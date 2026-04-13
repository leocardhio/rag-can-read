from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Config(BaseSettings):
  valid_content_types: List[str] = []
  
  postgres_user: str
  postgres_password: str
  postgres_db: str
  postgres_host: str
  postgres_port: str
  
  ollama_host: str | None
  ollama_model_name: str | None
  llm_model_name: str | None
  llm_base_url: str | None
  llm_api_key: str | None

  model_config = SettingsConfigDict(env_file='.env')