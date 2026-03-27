import os
import glob
import logging
import markdown

logging.basicConfig(level=logging.INFO, format="%(name)s - %(levelname)s - %(message)s")

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.dirname(BASE_PATH)

DOCS_PATH = os.path.join(BASE_PATH, "docs")
md_files = glob.glob(os.path.join(BASE_PATH, "docs", "**", "*.md"), recursive=True)

BUILD_PATH = os.path.join(BASE_PATH, "build")

logging.info(f"{BASE_PATH=}")
logging.info(f"Found {len(md_files)} markdown files in {DOCS_PATH}")

for file in md_files:
    logging.info(f"Processing {file} ...")
    with open(file, "r") as f:
        content = f.read()
        md = markdown.Markdown(extensions=['meta'])
        html = md.convert(content)
        print(md.Meta)
        
        title = md.Meta.get("title", ["Untitled"])[0]
        icon = md.Meta.get("icon", ["piano"])[0]
        break
