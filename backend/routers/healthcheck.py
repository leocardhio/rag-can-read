from fastapi import APIRouter, status

router = APIRouter(
  prefix="/health",
  tags=["healthcheck"],
  responses={
    400: {"message": "Bad Request"},
    500: {"message": "Internal Server Error"},
  }
)

@router.get('/', status_code=status.HTTP_200_OK)
def healthcheck():
  return {"message": "OK"}