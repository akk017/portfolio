import os
import json
from appwrite.client import Client
from appwrite.services.tables_db import TablesDB
from appwrite.id import ID


APPWRITE_ENDPOINT = os.getenv("APPWRITE_ENDPOINT", "https://sgp.cloud.appwrite.io/v1")
APPWRITE_PROJECT_ID = os.getenv("APPWRITE_PROJECT_ID")
APPWRITE_API_KEY = os.getenv("APPWRITE_API_KEY")
APPWRITE_DATABASE_ID = os.getenv("APPWRITE_DATABASE_ID")
APPWRITE_TABLE_ID = os.getenv("APPWRITE_TABLE_ID")

DATABASE_RESPONSE_DIR = "database-response"


def extract_record(db_response: dict) -> dict:
    """Extract relevant fields from a Notion database response JSON."""
    properties = db_response.get("properties", {})

    # Title from Name property
    name_prop = properties.get("Name", {})
    title_items = name_prop.get("title", [])
    title = title_items[0]["plain_text"] if title_items else ""

    # Source URL
    source_prop = properties.get("Source", {})
    source = source_prop.get("url") or ""

    # Tags from multi_select
    tags_prop = properties.get("Tags", {})
    tags_items = tags_prop.get("multi_select", [])
    tags = [tag["name"] for tag in tags_items]

    # URL property
    url_prop = properties.get("URL", {})
    url = url_prop.get("url") or ""

    # Created time
    created_time_prop = properties.get("Created time", {})
    created_time = created_time_prop.get("created_time", "")

    # Notion URL
    notion_url = db_response.get("url", "")

    # Image local path from blocks
    blocks = db_response.get("blocks", {})
    results = blocks.get("results", [])
    image_link = ""
    if results:
        block = results[0]
        if block.get("type") == "image":
            image_data = block.get("image", {})
            file_info = image_data.get("file", {})
            image_link = file_info.get("local_path", "")

    return {
        "record_id": db_response.get("id", ""),
        "title": title,
        "source": source,
        "tags": tags,
        "url": url,
        "created_time": created_time,
        "notion_url": notion_url,
        "image_link": image_link,
    }


def upload_to_appwrite(tables_db: TablesDB, record: dict) -> dict:
    """Upload a single record to Appwrite database table."""
    data = {
        "record_id": record["record_id"],
        "title": record["title"],
        "source": record["source"],
        "tags": record["tags"],
        "url": record["url"],
        "created_time": record["created_time"],
        "notion_url": record["notion_url"],
        "image_link": record["image_link"],
    }

    row = tables_db.create_row(
        database_id=APPWRITE_DATABASE_ID,
        table_id=APPWRITE_TABLE_ID,
        row_id=ID.unique(),
        data=data,
    )
    return row


def main():
    assert APPWRITE_PROJECT_ID is not None, "APPWRITE_PROJECT_ID not set"
    assert APPWRITE_API_KEY is not None, "APPWRITE_API_KEY not set"
    assert APPWRITE_DATABASE_ID is not None, "APPWRITE_DATABASE_ID not set"
    assert APPWRITE_TABLE_ID is not None, "APPWRITE_TABLE_ID not set"

    client = Client()
    client.set_endpoint(APPWRITE_ENDPOINT)
    client.set_project(APPWRITE_PROJECT_ID)
    client.set_key(APPWRITE_API_KEY)

    tables_db = TablesDB(client)

    db_files = sorted([
        f for f in os.listdir(DATABASE_RESPONSE_DIR)
        if f.endswith(".json")
    ])

    uploaded = 0
    failed = 0

    for db_file in db_files:
        filepath = os.path.join(DATABASE_RESPONSE_DIR, db_file)
        with open(filepath, "r") as f:
            db_response = json.load(f)

        record = extract_record(db_response)


        try:
            result = upload_to_appwrite(tables_db, record)
            uploaded += 1
            print(f"Uploaded: {record['title']} (Appwrite ID: ${result.id})")
        except Exception as e:
            failed += 1
            raise


    print(f"\nDone! Uploaded: {uploaded}, Failed: {failed}")


if __name__ == "__main__":
    main()
