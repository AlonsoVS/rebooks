from datetime import date
from marshmallow import fields, post_load
from src.app.shared.domain.database.db import db, BaseModel, ma, Base

class Review(Base, BaseModel):
  __tablename__ = 'reviews'
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(6000))
  publication_date = db.Column(db.Date)
  book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
  book = db.relationship('Book', back_populates='reviews')
  
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