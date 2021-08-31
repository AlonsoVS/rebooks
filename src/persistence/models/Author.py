from typing import List
from marshmallow import fields, post_load
from sqlalchemy.orm import validates
from src.persistence.db import Base, db, BaseModel, ma

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
 
class AuthorSchema(ma.Schema):
  id = fields.Integer()
  name = fields.String()
  books = fields.Nested('BookSchema', only=('id', 'name'), many=True)

  @post_load
  def set_author(self, data, **kwargs):
    return Author(**data)