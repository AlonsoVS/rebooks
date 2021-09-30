from flask_sqlalchemy.model import Model
from src.app.shared.domain.database.db import Base, db, BaseModel

class User(db.Model, Base, BaseModel):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(300))
  last_name = db.Column(db.String(300))
  username = db.Column(db.String(300))
  password = db.Column(db.String(300))

  def __init__(self, username:str, password:str, name:str="", last_name:str="", id:int=None):
    self.id = id
    self.name = name
    self.last_name = last_name
    self.username = username
    self.password = password
  
  @classmethod
  def find_by_username(cls, username):
    resp = cls.simple_filter(username=username)
    if (len(resp) > 0):
      return resp[0]
    return None

  def __repr__(self):
    return f'User:{self.__dict__}'