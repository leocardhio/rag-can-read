from functools import lru_cache

from .documents import DocumentsService

@lru_cache
def get_document_service():
  return DocumentsService()