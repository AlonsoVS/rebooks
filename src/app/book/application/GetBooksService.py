from src.app.book.domain.IBookRepository import IBookRepository
from src.app.book.application.GetBookResponse import GetBookResponse
from src.app.book.application.GetBooksResponse import GetBooksResponse

class GetBooksService():
  
  def __init__(self, repository:IBookRepository):
    self.repository = repository

  def get_all(self) -> GetBooksResponse:
    return GetBooksResponse(self.repository.get_all())
  
  def find_by_id(self, id:int) -> GetBookResponse:
    return GetBookResponse(self.repository.get(id))