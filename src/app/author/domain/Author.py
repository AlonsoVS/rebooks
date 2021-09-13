from typing import List

from marshmallow import fields, post_load
from src.app.shared.domain.database.db import ma

class Author():
  id:int = None
  name:str = None
  books = []

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