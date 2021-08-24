from typing import List
from marshmallow import fields, post_load
from src.persistence.db import Base, db, BaseModel, ma

class Author(Base, BaseModel):
  __tablename__ = 'authors'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(300))
  books = db.relationship('Book', secondary='books_authors')

  def __init__(self, name:str, books:List=[]):
    self.name = name
    self.books = books
  
  def __repr__(self):
    return f'Author:{self.__dict__}'
 
class AuthorSchema(ma.Schema):
  id = fields.Integer(dump_only=True)
  name = fields.String()
  books = fields.Pluck('BookSchema', 'name', many=True)

  @post_load
  def set_author(self, data, **kwargs):
    return Author(**data)