import fitz
from fastapi import UploadFile
from config import get_settings

class DocumentsService():
  async def process_content(self, file: UploadFile):
    config = get_settings()

    if file.content_type not in config.valid_content_types:
      raise TypeError("[Document Service] content type is not valid")
    
    content = await file.read()

    match file.content_type:
      case "application/pdf":
        return await self.__process_pdf(content)
      case "text/plain":
        return content
      
  async def __process_pdf(self, content: bytes):
    pdf = fitz.open(stream=content, filetype="pdf")
    
    text = ""
    for page in pdf:
        text += page.get_text()

    return text