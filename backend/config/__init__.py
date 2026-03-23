from .config import Config
from functools import lru_cache

@lru_cache
def get_settings():
  return Config()