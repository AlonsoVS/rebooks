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
    auth_token = request.headers.get('Authorization')
    if not auth_token:
      return {"message": "Authorization token is missing!"}, 401
    if (validate_token(auth_token)):
      current_user = get_current_user(auth_token)
      return func(current_user=current_user, *args, **kwargs)
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

def get_current_user(token: str):
  return jwt.decode(token, key, algorithms="HS256")

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