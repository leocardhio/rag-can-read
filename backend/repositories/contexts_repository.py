import logging
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from psycopg import Connection
from pgai.sqlalchemy import vectorizer_relationship

logger = logging.getLogger(__name__)

class Base(DeclarativeBase):
  pass

class ContextsRepository(Base):
  __tablename__ = 'contexts'
  
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column()
  content: Mapped[str] = mapped_column()
  
  context_embedding = vectorizer_relationship(dimensions=1024)
  
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