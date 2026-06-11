import os
import json
import time
import shutil
import logging
from abc import ABC, abstractmethod

import markdown
from fswatch import Monitor
from jinja2 import Environment, FileSystemLoader
from markdown.extensions import Extension

from compiler.configs import Config
from compiler.meta import Meta
from compiler.tree import PathNode


class BaseCompiler(ABC):
    @property
    @abstractmethod
    def config(self) -> "Config":
        raise NotImplementedError("abstract class")

    @abstractmethod
    def compile(self):
        raise NotImplementedError("abstract class")


class MDCompiler(BaseCompiler):
    def __init__(self, config: "Config", extensions: list[Extension|str]) -> None:
        super().__init__()
        self._config = config
        self._extention = extensions
        self._nav = []
        self._nav_dump = None

        self._loader = FileSystemLoader(
            os.path.join(self.config.base_path, "templates")
        )
        self._env = Environment(loader=self._loader)
        self._template = self._env.get_template("base.html")
        self._root = None

        self._md_meta = markdown.Markdown(extensions=["meta"])
        self._md = markdown.Markdown(extensions=self._extention)

        self._watch_files: list[PathNode] = []

    @property
    def config(self) -> "Config":
        return self._config

    @config.setter
    def config(self, value: "Config"):
        self._config = value

    @property
    def nav(self) -> list:
        return self._nav

    @nav.setter
    def nav(self, val):
        self._nav = val

    def compile(self):
        start = time.time()
        self._root = PathNode("root", self.config.docs_path)
        self.traverse_files(self.config.docs_path, self._root)
        self.nav = self.build_nav(self._root)
        self._nav_dump = json.dumps(self.nav, indent=2, ensure_ascii=False)

        shutil.rmtree(self.config.build_path, ignore_errors=True)
        os.mkdir(self.config.build_path)

        path = os.path.relpath(self.config.build_path, self.config.base_path)

        logging.info(f"building docs at {path=}")
        self.build_markdown(self._root)

        logging.info("moving templates to build")
        self.move_templates()

        logging.info("build complete")
        logging.info(f"build time: {time.time() - start:.2f}s")

    def watch(self):
        logging.info("---")
        logging.info("starting to watch files")

        path_to_node = {node.path.encode(): node for node in self._watch_files}

        def callback(path, *argv):
            node = path_to_node.get(path)
            if not node:
                logging.error("unable to get node")
                return
            self.build_page(node)

        watcher = Monitor()
        for node in self._watch_files:
            logging.info(f"watching file {node.name}")
            watcher.add_path(node.path)

        watcher.set_callback(callback)
        watcher.start()

    def traverse_files(self, path, root: PathNode):
        for name in os.listdir(path):
            child_path = os.path.join(path, name)
            node = PathNode(name, child_path)
            if ".md" in name:
                self.extract_meta(node)
                root.add_child(node)

            if os.path.isdir(child_path) and "." not in name:
                meta = Meta(title=name, slug=name)
                node.meta = meta
                root.add_child(node)
                self.traverse_files(path=child_path, root=node)

    def build_markdown(self, node: PathNode):
        for child in node.files:
            self.build_page(child)

        for dir in node.dirs:
            rel_path = dir.rel_path(self.config.docs_path)
            build_dir = os.path.join(self.config.build_path, rel_path)
            os.mkdir(build_dir)
            self.build_markdown(dir)

    def build_page(self, node: PathNode):
        try:
            with open(node.path, "r") as file:
                content = file.read()
        except FileNotFoundError:
            logging.error(f"file node found, {node.rel_path(self.config.docs_path)}")

        html = self._md.convert(content)
        rel_path = os.path.relpath(node.path, self.config.docs_path)
        if node.meta.slug:
            file_path = os.path.join(self.config.build_path, node.meta.slug) + ".md"
        else:
            file_path = os.path.join(self.config.build_path, rel_path)
        file_html_path = file_path.replace(".md", ".html")

        sources = self.parse_sources(node.meta.source)
        links = self.parse_sources(node.meta.links)

        with open(file_html_path, "w") as file:
            out = self._template.render(
                content=html,
                title=node.meta.title,
                sources=sources,
                links=links,
                date=node.meta.date,
                toc=self._md.toc,
                nav=self._nav_dump,
            )
            file.write(out)

        rel_path = os.path.relpath(file_path, self.config.build_path)
        logging.info(f"page build -> {rel_path}")

    def build_nav(self, node: PathNode) -> list:
        def convert(node: PathNode):
            if node.meta.slug:
                path = node.meta.slug
            else:
                path = node.rel_path(self.config.docs_path).replace(".md", ".html")

            if node.is_file:
                return {
                    "type": "Page",
                    "title": node.meta.title.lower(),
                    "href": "/" + path,
                    "folder": False,
                    "icon": "bookmark",
                }
            else:
                return {
                    "type": "Section",
                    "title": node.name.lower(),
                    "folder": True,
                    "children": [convert(c) for c in sorted(node.children, key=lambda n: n.path)],
                }

        return [convert(c) for c in sorted(node.children, key=lambda n: n.path)]

    def extract_meta(self, node: PathNode):
        with open(node.path, "r") as file:
            content = file.read()
            self._md_meta.convert(content)
            title = self._md_meta.Meta.get("title", ["Untitled"])[0]
            icon = self._md_meta.Meta.get("icon", ["piano"])[0]
            slug = self._md_meta.Meta.get("slug", [None])[0]
            date = self._md_meta.Meta.get("date", ["-- --- ----"])[0]
            sources = self._md_meta.Meta.get("sources", [])
            links = self._md_meta.Meta.get("links", [])
            watch = self._md_meta.Meta.get("watch", [False])[0]
            meta = Meta(
                title=title,
                icon=icon,
                slug=slug,
                date=date,
                source=sources,
                links=links,
                watch=watch,
            )
            node.meta = meta

            if watch:
                logging.info(f"added {node.rel_path(self.config.docs_path)} to watch")
                self._watch_files.append(node)

    def move_templates(self):
        static = os.path.join(self.config.build_path, "static")
        shutil.copytree(self.config.templates_path, static, dirs_exist_ok=True)

    @staticmethod
    def parse_sources(sources):
        parsed_sources = []
        if len(sources) == 0:
            return "NA"
        for source in sources:
            parsed_sources.append("<li>" + markdown.markdown(source) + "</li>")
        return '<ul class="source-list">' + "".join(parsed_sources) + "</ul>"
