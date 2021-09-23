from src.app.book.domain.IBookRepository import IBookRepository
from src.app.book.application.DeleteBookResponse import DeleteBookResponse
from src.app.book.domain.models.Book import Book

class DeleteBookService():
  def __init__(self, reposritory:IBookRepository):
    self.reposritory = reposritory
  
  def delete(self, id:int) -> DeleteBookResponse:
    book_found = self.reposritory.get(id)
    if (book_found is None):
      return DeleteBookResponse(id, False)
    self.reposritory.delete(id)
    return DeleteBookResponse(id, True)