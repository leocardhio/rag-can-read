from pydantic import BaseModel

class PromptType(BaseModel):
  message: str