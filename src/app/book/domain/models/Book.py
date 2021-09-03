from datetime import date
from src.app.author.domain.models.Author import Author
from src.app.review.domain.models.Review import Review
from typing import List
from marshmallow import fields, post_load
from src.app.shared.domain.database.db import db, BaseModel, ma, Base
from  sqlalchemy import Column, Table

books_authors_association = Table(
  'books_authors', Base.metadata,
  Column('book_id', db.Integer, db.ForeignKey('books.id')),
  Column('author_id', db.Integer, db.ForeignKey('authors.id'))
)

class Book(Base, BaseModel):
  __tablename__ = 'books'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  cover = db.Column(db.String())
  abstract = db.Column(db.String())
  publication_date = db.Column(db.Date)
  reviews = db.relationship('Review', cascade='all, delete-orphan', back_populates='book')
  authors = db.relationship('Author', secondary='books_authors')

  def __init__(self, 
                name:str,
                cover:str='', 
                abstract:str='',
                publication_date:date=None, 
                reviews:List[Review]=[],
                authors:List[Author]=[]
              ):
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