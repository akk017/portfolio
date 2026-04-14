import os
import sys
import json
import uuid
import random
import requests


API_URL = "https://api.notion.com/v1"
API_TOKEN = os.getenv("NOTION_API_TOKEN")
# assert API_TOKEN is not None

DATABASE_ID = "1e325a6056fb43299d36f04b0c0fbd75"

TAG_COLORS = [
    'skyblue', 'plum', 'aqua', 'aquamarine', 'coral', 'gold',
    'lightblue', 'lightgreen', 'lightpink', 'lightsalmon',
    'mediumspringgreen', 'mediumturquoise', 'mediumorchid',
    'palevioletred', 'paleturquoise', 'palegreen', 'palegoldenrod',
    'tomato', 'turquoise', 'violet'
]


def get_database():
    url = f"{API_URL}/databases/{DATABASE_ID}/query"
    headers = {
        "User-Agent": "yaak",
        "Accept": "*/*",
        "Authorization": f"Bearer {API_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }

    os.makedirs("database-response", exist_ok=True)

    start_cursor = None
    count = 0

    while True:
        payload = {}
        if start_cursor:
            payload["start_cursor"] = start_cursor

        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        results = data.get("results", [])

        for result in results:
            count += 1
            filename = f"database-response/database-response-{count}.json"
            with open(filename, "w") as f:
                json.dump(result, f, indent=2)
            print(f"Saved {filename}")

        if not data.get("has_more"):
            break

        start_cursor = data.get("next_cursor")

    print(f"Saved {count} files total")


def get_pages():
    os.makedirs("page-response", exist_ok=True)

    headers = {
        "User-Agent": "yaak",
        "Accept": "*/*",
        "Authorization": f"Bearer {API_TOKEN}",
        "Notion-Version": "2026-03-11",
        "Content-Type": "application/json",
    }

    database_files = sorted([
        f for f in os.listdir("database-response")
        if f.endswith(".json")
    ])

    count = 1

    for db_file in database_files:
        filepath = os.path.join("database-response", db_file)
        with open(filepath, "r") as f:
            page_data = json.load(f)

        page_id = page_data.get("id")
        assert page_id is not None

        url = f"{API_URL}/blocks/{page_id}/children"

        response = requests.get(url, headers=headers)
        filename = f"page-response/response-{count}.json"
        count += 1

        with open(filename, "w") as f:
            json.dump(response.json(), f, indent=2)
        
        print(f"Saved {filename}")            

    print(f"Saved {count} files total")

def get_images():
    os.makedirs("images", exist_ok=True)

    page_files = sorted([
        f for f in os.listdir("page-response")
        if f.endswith(".json")
    ])

    for page_file in page_files:
        filepath = os.path.join("page-response", page_file)
        with open(filepath, "r") as f:
            data = json.load(f)

        results = data.get("results", [])
        if not results:
            continue

        block = results[0]
        block_type = block.get("type")
        block_id = block.get("id")
        partent_id = block.get("parent").get("page_id")

        if block_type == "image":
            image_data = block.get("image", {})
            file_info = image_data.get("file", {})
            url = file_info.get("url")

            if url:
                img_response = requests.get(url)
                img_filename = f"{uuid.uuid4()}.jpg"
                img_path = os.path.abspath(os.path.join("images", img_filename))

                with open(img_path, "wb") as f:
                    f.write(img_response.content)

                file_info["local_path"] = img_path

                with open(filepath, "w") as f:
                    json.dump(data, f, indent=2)

                print(f"Saved image to {img_path}")
        else:
            print(f"image not for {block_id}")


def link():
    page_files = sorted([
        f for f in os.listdir("page-response")
        if f.endswith(".json")
    ])

    page_data = {}

    for file in page_files:
        with open("./page-response/" + file, "r") as f:
            data = json.load(f)
            results = data.get("results", [])
            if not results:
                continue

            block = results[0]
            block_id = block.get("parent").get("page_id")

            page_data[block_id] = data

    database_file = sorted([
        f for f in os.listdir("database-response")
        if f.endswith(".json")
    ])

    for file in database_file:
        with open("./database-response/" + file) as f:
            database_data = json.load(f)
            k = database_data["id"]
            try:
                database_data["blocks"] = page_data[k]
            except KeyError:
                with open("empty.txt", "a") as em:
                    em.write(k + '\n')

        with open("./database-response/" + file, "w") as f:
            json.dump(database_data, f, indent=2)

        print(f"succes, {k}")

def mongo_tags():
    tags_file = "/Users/akash-21652/Projects/portfolio/tags.md"
    with open(tags_file, "r") as f:
        tags = [line.strip() for line in f if line.strip()]

    url = "http://localhost:9003/api/v1/mongo/bulk-insert"
    headers = {
        "User-Agent": "yaak",
        "Accept": "*/*",
        "Content-Type": "application/json",
    }

    documents = [
        {"name": tag, "color": random.choice(TAG_COLORS)}
        for tag in tags
    ]

    payload = {
        "collection": "tags",
        "documents": documents
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    print(f"Inserted {data.get('count', len(tags))} tags")

    for tag in tags:
        print(f"Created tag: {tag}")


def main():
    if len(sys.argv) != 3 or sys.argv[1] != "type":
        print("Usage: python test.py type <database|pages|images|link|mongo-tags>")
        sys.exit(1)

    query_type = sys.argv[2]

    if query_type == "database":
        get_database()
    elif query_type == "pages":
        get_pages()
    elif query_type == "images":
        get_images()
    elif query_type == "link":
        link()
    elif query_type == "mongo-tags":
        mongo_tags()
    else:
        print("Invalid type. Use 'database', 'pages', 'images', 'link', or 'mongo-tags'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
