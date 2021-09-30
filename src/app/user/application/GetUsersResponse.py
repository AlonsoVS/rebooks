from src.app.user.domain.models.User import User
from src.app.user.domain.User import UserSchema
from typing import List

class GetUsersResponse():
  def __init__(self, users:List[User]):
    self.users = users
  
  def get_users(self) -> List[User]:
    return self.users
