from marshmallow import fields, post_load
from src.app.shared.domain.database.db import ma

class User():
  __tablename__ = 'users'

  def __init__(self, username:str, password:str, name:str="", last_name:str="", id:int=None):
    self.id = id
    self.name = name
    self.last_name = last_name
    self.username = username
    self.password = password
  
  def find_by_username(cls, username):
    return cls.simple_filter(username=username)[0]

  def __repr__(self):
    return f'User:{self.__dict__}'

class UserSchema(ma.Schema):
  id = fields.Integer()
  name = fields.String()
  last_name = fields.String()
  username = fields.String()
  password = fields.String()

  @post_load
  def set_author(self, data, **kwargs):
    return User(**data)