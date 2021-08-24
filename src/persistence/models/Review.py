from datetime import date
from marshmallow import fields, post_load
from src.persistence.db import db, BaseModel, ma, Base

class Review(Base, BaseModel):
  __tablename__ = 'reviews'
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(6000))
  publication_date = db.Column(db.Date)
  book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
  
  def __init__(self, content:str, book_id:int, publication_date:date=None):
    self.content = content
    self.publication_date = publication_date
    self.book_id = book_id
  
  def __repr__(self):
    return f'Review:{self.__dict__}'
 
class ReviewSchema(ma.Schema):
  id = fields.Integer(dump_only=True)
  content = fields.String()
  publication_date = fields.Date()
  book_id = fields.Integer()

  @post_load
  def make_review(self, data, **kwargs):
    return Review(**data)