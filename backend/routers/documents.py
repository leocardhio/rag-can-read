from fastapi import APIRouter, status, UploadFile
from services import get_document_service

router = APIRouter(
  prefix="/documents",
  tags=["documents"],
  responses={
    400: {"message": "Bad Request"},
    500: {"message": "Internal Server Error"},
  }
)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def upload_document(file: UploadFile):
  processed_content = await get_document_service().process_content(file)

  return {
    "filenames": file.filename,
    "contents": processed_content
  }