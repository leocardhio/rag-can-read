from fastapi import APIRouter, status

router = APIRouter(
  prefix="/chat",
  tags=["chat"],
  responses={
    400: {"message": "Bad Request"},
    500: {"message": "Internal Server Error"},
  }
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def post_chat():
  return {"message": "Chat created"}