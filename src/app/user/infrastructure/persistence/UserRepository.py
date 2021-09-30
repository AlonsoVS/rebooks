from typing import List, Optional
from src.app.user.domain.User import User
from src.app.user.domain.models.User import User as UserModel
from src.app.user.domain.IUserRepository import IUserRepository

class UserRepository(IUserRepository):
  def save(self, user: User) -> Optional[User]:
    new_user = UserModel(name=user.name,
                        last_name=user.last_name,
                        username=user.username,
                        password=user.password)
    new_user.save()
    return new_user

  def get(self, user_id: int) -> Optional[User]:
    return UserModel.get_by_id(user_id)
  
  def get_by_username(self, username: str) -> Optional[User]:
      return UserModel.find_by_username(username)

  def get_all(self) -> List[User]:
    return UserModel.get_all()
  
  def update(self, user:dict) -> Optional[User]:
    user_to_update = UserModel.get_by_id(user["id"])
    if user_to_update is not None:
      for key in user.keys():
        if (key != "id"):
          try:
            setattr(user_to_update, key, user[key])
          except:
            return None
    else:
      return None
    user_to_update.save()
    return user_to_update

  def delete(self, user_id: int):
    user = UserModel.get_by_id(user_id)
    user.delete()