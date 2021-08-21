from marshmallow import fields, post_load
from src.persistence.db import Base, db, BaseModel, ma

class Author(db.Model, Base, BaseModel):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(300))
  
  def __init__(self, name:str):
    self.name = name
  
  def __repr__(self):
    return f'Author:{self.__dict__}'
 
class AuthorSchema(ma.Schema):
  id = fields.Integer(dump_only=True)
  name = fields.String()

  @post_load
  def set_author(self, data, **kwargs):
    return Author(**data)