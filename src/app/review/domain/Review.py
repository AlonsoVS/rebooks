from src.app.book.domain.Book import Book
from src.app.shared.domain.database.db import ma
from marshmallow import fields, post_load
from datetime import date

class Review():
  id:int = None
  content:str = None
  publication_date:date = None
  book_id:int = None
  book:Book = None
  
  def __init__(self, content:str, book_id:int=None, publication_date:date=None):
    self.content = content
    self.publication_date = publication_date
    self.book_id = book_id
  
  def __repr__(self):
    return f'Review:{self.__dict__}'

class ReviewSchema(ma.Schema):
  id = fields.Integer()
  content = fields.String()
  book_id = fields.Integer()
  publication_date = fields.Date()
  book = fields.Pluck('BookSchema', "name")

  @post_load
  def make_review(self, data, **kwargs):
    return Review(**data)