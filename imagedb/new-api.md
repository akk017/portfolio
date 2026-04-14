curl -X POST 'http://localhost:9003/api/v1/mongo/read_all' \
  --header 'User-Agent: yaak' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data '{
  "collection": "tags"
}'

{
  "count": 4,
  "documents": [
    {
      "color": "pink",
      "id": "69d4cb12eeb883bc77458474",
      "name": "Test"
    },
    {
      "color": "pink",
      "id": "69d4cb12eeb883bc77458475",
      "name": "Test"
    },
    {
      "color": "pink",
      "id": "69d4cb12eeb883bc77458476",
      "name": "Test"
    },
    {
      "color": "pink",
      "id": "69d4cb955a47e0a603453175",
      "name": "Test"
    }
  ]
}

---

curl -X POST 'http://localhost:9003/api/v1/mongo/create' \
  --header 'User-Agent: yaak' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data '{
  "collection": "tags",
  "document": {
    "name": "Test",
    "color": "pink"
  }
}'

{
  "inserted_id": "69d4cb955a47e0a603453175"
}

curl -X POST 'http://localhost:9003/api/v1/mongo/read' \
  --header 'User-Agent: yaak' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data '{
  "collection": "tags",
  "id": "69d4cac4eeb883bc77458473",
}'

{
  "color": "pink",
  "id": "69d4cac4eeb883bc77458473",
  "name": "Test"
}

curl -X POST 'http://localhost:9003/api/v1/mongo/read' \
  --header 'User-Agent: yaak' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data '{
  "collection": "tags",
  "id": "69d4cb12eeb883bc77458474",
}'

{
  "document": {
    "color": "pink",
    "id": "69d4cb12eeb883bc77458474",
    "name": "Test"
  },
  "id": "69d4cb12eeb883bc77458474"
}

