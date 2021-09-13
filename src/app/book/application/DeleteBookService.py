from src.app.book.application.DeleteBookResponse import DeleteBookResponse
from src.app.book.domain.models.Book import Book

class DeleteBookService():
  def __init__(self):
    return
  
  def delete(self, id:int) -> DeleteBookResponse:
    book_found = Book.get_by_id(id)
    if (book_found is None):
      return DeleteBookResponse(id, False)
    book_found.delete()
    return DeleteBookResponse(id, True)