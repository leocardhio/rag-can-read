from functools import lru_cache

from .documents import DocumentsService
from .llm import LLMService

@lru_cache
def get_document_service():
  return DocumentsService()

@lru_cache
def get_llm_service():
  return LLMService()