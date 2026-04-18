import logging
from psycopg import Connection

logger = logging.getLogger(__name__)

class EmbeddingsRepository():
  def __init__(self, db_connection: Connection):
    self.connection = db_connection
    
    self.__create_table()
    
  def __create_table(self):
    self.connection.execute()
    logger.info("Ensured embeddings table exists")

  def find_all(self):
    return self.connection.execute('SELECT * FROM embeddings').fetchall()
  
  def insert_one(self):
    self.connection.execute('INSERT INTO embeddings(...) VALUES (...)')