from psycopg import Connection

class ChatHistoryRepository():
  def __init__(self, db_connection: Connection):
    self.connection = db_connection

  def find_all(self):
    return self.connection.execute('SELECT * FROM chat_histories').fetchall()
  
  def insert_one(self):
    self.connection.execute('INSERT INTO chat_histories (...) VALUES (...)')

  def clear_chat(self):
    self.connection.execute('DELETE FROM chat_histories')