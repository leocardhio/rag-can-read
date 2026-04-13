import psycopg
from pgvector.psycopg import register_vector
from functools import lru_cache

from config import get_settings

from .embeddings_repository import EmbeddingsRepository
from .chat_history_repository import ChatHistoryRepository


db_connection = psycopg.connect(
  dbname=get_settings().postgres_db,
  host=get_settings().postgres_host,
  user=get_settings().postgres_user,
  password=get_settings().postgres_password,
  port=get_settings().postgres_port
)

db_connection.execute('CREATE EXTENSION IF NOT EXISTS ai')
db_connection.execute('CREATE EXTENSION IF NOT EXISTS vector')
db_connection.execute('CREATE EXTENSION IF NOT EXISTS vectorscale CASCADE')

register_vector(db_connection)

@lru_cache
def get_repositories():
  return {
    "embeddings": EmbeddingsRepository(db_connection),
    "chat_history": ChatHistoryRepository(db_connection)
  }