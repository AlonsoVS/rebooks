from src.app.user.application.DeleteUserResponse import DeleteUserResponse
from src.app.user.domain.IUserRepository import IUserRepository

class DeleteUserService():
  def __init__(self, repository: IUserRepository):
    self.repository = repository
  
  def delete(self, id:int):
    user_found = self.repository.get(id)
    if (user_found is None):
      return DeleteUserResponse(id, False)
    self.repository.delete(id)
    return DeleteUserResponse(id, True)