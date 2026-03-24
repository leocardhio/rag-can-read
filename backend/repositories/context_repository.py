from psycopg import Connection

class ContextRepository():
  def __init__(self, db_connection: Connection):
    self.connection = db_connection

  def find_all(self):
    return self.connection.execute('SELECT * FROM contexts').fetchall()
  
  def insert_one(self):
    self.connection.execute('INSERT INTO contexts(...) VALUES (...)')