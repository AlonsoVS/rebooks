from src.app.user.infrastructure.persistence.UserRepository import UserRepository
from src.app.user.domain.models.User import User
from src.app.user.application.GetUsersService import GetUsersService
from flask import request
from functools import wraps
from datetime import datetime, timedelta
import jwt

key = 'My-custom-api-key'

def auth_token_required(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    header = request.headers.get('Authorization')
    if not header:
      return {"message": "Authorization token is missing!"}, 401
    if (validate_token(header)):
      return func(*args, **kwargs)
    return {"message": "Authorization Token is invalid!"}, 401
  return wrapper

def create_token(username:str, password:str):
  auth_data = {"username": username, "password": password}
  if (validate_auth_data(auth_data)):
    token = jwt.encode({
        "username": username,
        "password": password,
        "exp": datetime.utcnow() + timedelta(minutes = 20),
    }, key, algorithm="HS256")
    return token
  return None

def validate_auth_data(data:dict):
  user:User = GetUsersService(UserRepository()).find_by_username(data["username"]).get_user()
  if (user and data["password"] == user.password):
    return True
  return False

def validate_token(token:str):
  try:
    data = jwt.decode(token, key, algorithms="HS256")
    if (validate_auth_data(data)):
      return True
  except:
    return False