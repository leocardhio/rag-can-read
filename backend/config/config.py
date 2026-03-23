from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Config(BaseSettings):
  valid_content_types: List[str] = []

  model_config = SettingsConfigDict(env_file='.env')