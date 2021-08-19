from datetime import date
from marshmallow import fields, post_load
from src.persistence.db import db, BaseModel, ma

class Review(db.Model, BaseModel):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(6000))
  publication_date = db.Column(db.Date)
  
  def __init__(self, content:str, publication_date:date=None):
    self.content = content
    self.publication_date = publication_date
  
  def __repr__(self):
    return f'Review:{self.__dict__}'
 
class ReviewSchema(ma.Schema):
  id = fields.Integer(dump_only=True)
  content = fields.String()
  publication_date = fields.Date()

  @post_load
  def make_review(self, data, **kwargs):
    return Review(**data)