from typing import List, Optional
from src.app.book.domain.Book import Book
from abc import ABCMeta, abstractmethod

class IBookRepository(metaclass=ABCMeta):
  @abstractmethod
  def save(self, book:Book) -> Optional[Book]:
    pass
  
  @abstractmethod
  def get(self, book_id:int) -> Optional[Book]:
    pass

  @abstractmethod
  def get_all(self) -> List[Book]:
    pass
  
  @abstractmethod
  def update(self, book:Book) -> Optional[Book]:
    pass

  @abstractmethod
  def delete(self, book_id:int):
    pass 