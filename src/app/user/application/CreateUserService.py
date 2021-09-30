from src.app.user.domain.IUserRepository import IUserRepository
from src.app.user.application.CreateUserResponse import CreateUserResponse
from src.app.user.domain.User import User, UserSchema

class CreateUserService():
  def __init__(self, repository: IUserRepository):
    self.repository = repository
  
  def create(self, user_data:dict):
    new_user:User = UserSchema().load(user_data)
    return CreateUserResponse(self.repository.save(new_user))