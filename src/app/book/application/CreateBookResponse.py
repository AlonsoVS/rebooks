from typing import Optional
from src.app.book.domain.models.Book import Book
from src.app.book.domain.Book import BookSchema

class CreateBookResponse():
  def __init__(self, book:Optional[Book]=None):
    self.book = book
  
  def created(self):
    if (self.book is None):
      return False
    return BookSchema().dump(self.book)