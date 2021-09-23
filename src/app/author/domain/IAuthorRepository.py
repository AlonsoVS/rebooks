from typing import List, Optional
from src.app.author.domain.Author import Author
from abc import ABCMeta, abstractmethod

class IAuthorRepository(metaclass=ABCMeta):
  @abstractmethod
  def save(self, author:Author) -> Optional[Author]:
    pass
  
  @abstractmethod
  def get(self, author_id:int) -> Optional[Author]:
    pass

  @abstractmethod
  def get_all(self) -> List[Author]:
    pass
  
  @abstractmethod
  def update(self, author:Author) -> Optional[Author]:
    pass

  @abstractmethod
  def delete(self, author_id:int):
    pass 