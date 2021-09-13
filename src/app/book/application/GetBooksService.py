from src.app.book.application.GetBookResponse import GetBookResponse
from src.app.book.application.GetBooksResponse import GetBooksResponse
from src.app.book.domain.models.Book import Book

class GetBooksService():
  
  def __init__(self):
    return

  def get_all(self) -> GetBooksResponse:
    return GetBooksResponse(Book.get_all())
  
  def find_by_id(self, id:int) -> GetBookResponse:
    return GetBookResponse(Book.get_by_id(id))