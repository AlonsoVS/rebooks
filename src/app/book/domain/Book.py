from datetime import date
from marshmallow import fields, post_load
from src.app.author.domain.Author import Author
from typing import List
from src.app.review.domain.models.Review import Review
from src.app.shared.domain.database.db import ma

class Book():
  def __init__(self, 
                name:str,
                id:int=None,
                cover:str='', 
                abstract:str='',
                publication_date:date=None, 
                reviews:List[Review]=[],
                authors:List[Author]=[]
              ):
    self.id = id
    self.name = name
    self.cover = cover
    self.abstract = abstract
    self.reviews = reviews
    self.publication_date = publication_date
    self.authors = authors
  
  def __repr__(self):
    return f'Book:{self.__dict__}'

class BookSchema(ma.Schema):
  id = fields.Integer()
  name = fields.String()
  cover = fields.String()
  abstract = fields.String()
  publication_date = fields.Date()
  reviews = fields.Nested('ReviewSchema', only=("id", "content", "publication_date"), many=True)
  authors = fields.Nested('AuthorSchema', only=("name","id"), many=True)

  @post_load
  def make_book(self, data, **kwargs):
    return Book(**data)