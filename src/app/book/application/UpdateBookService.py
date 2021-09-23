from src.app.book.domain.IBookRepository import IBookRepository
from src.app.book.application.UpdateBookResponse import UpdateBookResponse

class UpdateBookService():
  def __init__(self, repository:IBookRepository):
    self.repository = repository
  
  def update(self, update_data:dict) -> UpdateBookResponse:
    return UpdateBookResponse(self.repository.update(update_data))