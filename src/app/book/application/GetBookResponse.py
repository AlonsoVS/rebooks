from typing import Optional
from src.app.book.domain.models.Book import Book
from src.app.book.domain.Book import BookSchema

class GetBookResponse():
  def __init__(self, book:Book):
    self.book = book
  
  def get_book(self) -> Optional[Book]:
    if (self.book is not None):
      return BookSchema().dump(self.book)
    return None