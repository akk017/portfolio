import logging
import json

from mkdocs.plugins import BasePlugin
from mkdocs.utils.meta import get_data

log = logging.getLogger(f"mkdocs.plugins.{__name__}")

def populate_nav(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            defn = json.load(f)
        val = json.dumps(defn)
        log.info("Nav Config Loaded Successfully")
        return val
    except Exception:
        log.error("Nav File Not Found")


class NavToJsonPlugin(BasePlugin):
    def __init__(self):
        self.page_meta = {}

    def on_env(self, env, /, *, config, files):
        env.filters["populate_nav"] = populate_nav

    def on_nav(self, nav, config, files):
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