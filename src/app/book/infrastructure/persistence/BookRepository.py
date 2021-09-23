from src.app.review.domain.models.Review import Review
from src.app.author.domain.models.Author import Author
from typing import List, Optional
from src.app.book.domain.Book import Book
from src.app.book.domain.models.Book import Book as BookModel
from src.app.book.domain.IBookRepository import IBookRepository

class BookRepository(IBookRepository):
  def __init__(self):
    pass

  def save(self, new_book:Book) -> Optional[Book]:
    book = BookModel(name=new_book.name,
                     cover=new_book.cover,
                     abstract=new_book.abstract,
                     publication_date=new_book.publication_date)
    
    for author in new_book.authors:
      if author.id is None:
        book.authors.append(Author(author.name))
      else:
        author_found = author.get_by_id(author.id)
        if (author_found is not None):
          book.authors.append(author_found)
        else:
          return None
    
    for review in new_book.reviews:
      book.reviews.append(Review(content=review.content, 
                                publication_date=review.publication_date))
    book.save()
    return book

  def get(self, book_id: int) -> Optional[Book]:
    return BookModel.get_by_id(book_id)

  def get_all(self) -> List[Book]:
    books = BookModel.get_all();
    return books
  
  def update(self, book: dict) -> Optional[Book]:
    book_to_update = BookModel.get_by_id(book["id"])
    if book_to_update is not None:
      for key in book.keys():
        if (key != "id"):
          try:
            setattr(book_to_update, key, book[key])
          except:
            return None
    else:
      return None
    book_to_update.save()
    return book_to_update

  def delete(self, book_id: int):
    book = BookModel.get_by_id(book_id)
    book.delete()