from src.app.book.domain.models.Book import Book
from src.app.book.domain.Book import BookSchema
from typing import List

class GetBooksResponse():
  def __init__(self, books:List[Book]):
    self.books = books
  
  def get_books(self) -> List[Book]:
    return BookSchema().dump(self.books, many=True)
