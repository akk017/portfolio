from typing import Annotated

from fastapi import UploadFile, APIRouter
from .processor.ocr import OCRProcessor

router = APIRouter(prefix="/images")

@router.post("/tag")
async def create_upload_file(image: UploadFile):
    text = await OCRProcessor.process(image)
    return {"text": text}

