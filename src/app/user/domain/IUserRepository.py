from typing import List, Optional
from src.app.user.domain.User import User
from abc import ABCMeta, abstractmethod

class IUserRepository(metaclass=ABCMeta):
  @abstractmethod
  def save(self, user:User) -> Optional[User]:
    pass
  
  @abstractmethod
  def get(self, user_id:int) -> Optional[User]:
    pass

  @abstractmethod
  def get_by_username(self, username:str) -> Optional[User]:
    pass

  @abstractmethod
  def get_all(self) -> List[User]:
    pass
  
  @abstractmethod
  def update(self, user:User) -> Optional[User]:
    pass

  @abstractmethod
  def delete(self, user_id:int):
    pass 