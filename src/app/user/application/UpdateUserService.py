from src.app.user.domain.IUserRepository import IUserRepository
from src.app.user.application.UpdateUserResponse import UpdateUserResponse

class UpdateUserService():
  def __init__(self, repository:IUserRepository):
    self.repository = repository
  
  def update(self, update_data:dict) -> UpdateUserResponse:
    return UpdateUserResponse(self.repository.update(update_data))