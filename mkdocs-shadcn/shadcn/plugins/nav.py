import logging
import json

from mkdocs.plugins import BasePlugin
from mkdocs.utils.meta import get_data

import os

log = logging.getLogger(f"mkdocs.plugins.{__name__}")

def populate_nav(filename):
    log.info("Test Log")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            defn = json.load(f)
        val = json.dumps(defn)
        log.info("Nav Config Loaded Successfully")
        return val
    except Exception:
        log.error("Nav File Not Found")


def last_commit(arg):
    commit = os.getenv("LAST_COMMIT")
    branch = "main"
    log.info(f"Last Commit => {branch=} {commit=}")
    return commit


class NavToJsonPlugin(BasePlugin):
    def __init__(self):
        self.page_meta = {}

    def on_env(self, env, /, *, config, files):
        env.filters["populate_nav"] = populate_nav
        env.filters["last_commit"] = last_commit

    def on_nav(self, nav, config, files):
        last_commit = os.getenv("LAST_COMMIT")
        log.info("Getting Meta for Nav")
        def convert(item):
            if item.is_page:
                doc, meta = get_data(item.file.content_string)
                title = meta.get("title")
                icon = meta.get("icon")
                return {
                    "type": "Page",
                    "title": title,
                    "href": "/" + item.url,
                    "folder": False,
                    "icon": icon
                }
            else:
                return {
                    "type": "Section",
                    "title": item.title,
                    "children": [convert(c) for c in item.children],
                    "folder": True,
                }

        nav_json = [convert(i) for i in nav]
        with open("nav.json", "w", encoding="utf-8") as f:
            json.dump(nav_json, f, indent=2, ensure_ascii=False)
        log.info("Nav Stored Successfully")
        return nav