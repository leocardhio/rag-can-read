from .config import Config
from functools import lru_cache

def __enhance_config_with_ollama_fallback(config: Config) -> Config:
  config.llm_base_url = config.llm_base_url or config.ollama_host
  config.llm_model_name = config.llm_model_name or config.ollama_model_name
    
  return config

@lru_cache
def get_settings():
  config = Config()
  return __enhance_config_with_ollama_fallback(config)