from typing import List
from src.app.shared.domain.database.db import Base, db, BaseModel

class Author(Base, BaseModel):
  __tablename__ = 'authors'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(300))
  books = db.relationship('Book', secondary='books_authors')

  def __init__(self, name:str, id:int=None, books:List=[]):
    self.id = id
    self.name = name
    self.books = books
  
  def __repr__(self):
    return f'Author:{self.__dict__}'