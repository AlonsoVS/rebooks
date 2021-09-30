from src.app.user.application.GetUserResponse import GetUserResponse
from src.app.user.application.GetUsersResponse import GetUsersResponse
from src.app.user.domain.IUserRepository import IUserRepository

class GetUsersService():
  def __init__(self, repository: IUserRepository):
    self.repository = repository

  def get_all(self):
    return GetUsersResponse(self.repository.get_all())
  
  def find_by_id(self, id: int):
    return GetUserResponse(self.repository.get(id))
  
  def find_by_username(self, username: str):
    return  GetUserResponse(self.repository.get_by_username(username))