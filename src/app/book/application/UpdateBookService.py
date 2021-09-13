from src.app.book.application.UpdateBookResponse import UpdateBookResponse
from src.app.book.domain.models.Book import Book

class UpdateBookService():
  def __init__(self):
    return
  
  def update(self, book_id:int, update_data:dict):
    if book_id is not None:
      book_to_update:Book = Book.get_by_id(book_id)
      if book_to_update is not None:
        for key in update_data.keys():
          try:
            setattr(book_to_update, key, update_data[key])
          except:
            return UpdateBookResponse()
      else:
        return UpdateBookResponse()
      book_to_update.save()
      return UpdateBookResponse(book_to_update)
    return UpdateBookResponse()