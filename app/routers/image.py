from fastapi import APIRouter, UploadFile, File
from app.utils.image_processing import process_image

router = APIRouter()

@router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    result = await process_image(file)
    return {"result": result}
