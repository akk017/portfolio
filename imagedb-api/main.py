# main.py
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from upload.tagger import router

import uvicorn

class Tag(BaseModel):
    tag: str


app = FastAPI()
app.include_router(router, prefix="/api/v1")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tags = ["dev", "animation", "design", "collection", "saas", "opensource"]

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/api/tags")
def get_tags():
    return tags

@app.post("/api/tags")
def create_tag(data: Tag):
    tags.append(data.tag)
    return tags

@app.delete("/api/tags")
def delete_tag(data: Tag):
    if data.tag not in tags:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    tags.remove(data.tag)
    return tags


if __name__ == "__main__":
    uvicorn.run(app, port=8080)