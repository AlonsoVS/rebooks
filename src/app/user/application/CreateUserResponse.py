from typing import Optional
from src.app.user.domain.models.User import User
from  src.app.user.domain.User import User as UserDomain
from src.app.user.domain.User import UserSchema

class CreateUserResponse():
  def __init__(self, user:Optional[User]=None):
    self.user = user
  
  def created(self) -> Optional[UserDomain]:
    if (self.user is None):
      return False
    return UserSchema().dump(self.user)