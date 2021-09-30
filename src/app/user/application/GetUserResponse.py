from typing import Optional
from src.app.user.domain.models.User import User
from src.app.user.domain.User import UserSchema

class GetUserResponse():
  def __init__(self, user: User):
    self.user = user
  
  def get_user(self) -> Optional[User]:
    if (self.user is not None):
      return self.user
    return None