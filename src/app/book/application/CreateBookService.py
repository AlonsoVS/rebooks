from src.app.book.domain.IBookRepository import IBookRepository
from src.app.book.application.CreateBookResponse import CreateBookResponse
from src.app.book.domain.Book import Book

class CreateBookService():
  def __init__(self, repository:IBookRepository):
    self.repository = repository
  
  def create(self, new_book:Book) -> CreateBookResponse:
    return CreateBookResponse(self.repository.save(new_book))