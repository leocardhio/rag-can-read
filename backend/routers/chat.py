from fastapi import APIRouter, status
from services import get_llm_service
from custom_types import PromptType

router = APIRouter(
  prefix="/chat",
  tags=["chat"],
  responses={
    400: {"message": "Bad Request"},
    500: {"message": "Internal Server Error"},
  }
)

LLMService = get_llm_service()

@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_chat(prompt: PromptType):
  response = await LLMService.generate(prompt.message)
  return {"response": response}
  