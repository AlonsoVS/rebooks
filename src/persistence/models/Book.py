from datetime import date
from src.persistence.models.Author import Author
from src.persistence.models.Review import Review
from typing import List
from marshmallow import fields, post_load
from src.persistence.db import db, BaseModel, ma

class Book(db.Model, BaseModel):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(300))
  cover = db.Column(db.String(200))
  abstract = db.Column(db.String(600))
  publication_date = db.Column(db.Date)
  reviews = db.relationship('Review', cascade='all, delete-orphan')

  def __init__(self, 
                name:str, 
                cover:str='', 
                abstract:str='',
                authors:List[Author]=[],
                publication_date:date=None, 
                reviews:List[Review]=[]
              ):
    self.name = name
    self.cover = cover
    self.abstract = abstract
    self.publication_date = publication_date
    self.reviews = reviews
    self.authors = authors
  
  def __repr__(self):
    return f'Book:{self.__dict__}'

class BookSchema(ma.Schema):
  id = fields.Integer(dump_only=True)
  name = fields.String()
  cover = fields.String()
  abstract = fields.String()
  publication_date = fields.Date()
  reviews = fields.Nested('ReviewSchema', many=True)
  authors = fields.Nested('AuthorSchema', many=True)

  @post_load
  def make_book(self, data, **kwargs):
    return Book(**data)