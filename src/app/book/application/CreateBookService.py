from src.app.book.application.CreateBookResponse import CreateBookResponse
from src.app.review.domain.models.Review import Review
from src.app.author.domain.models.Author import Author
from src.app.book.domain.Book import Book
from src.app.book.domain.models.Book import Book as BookModel

class CreateBookService():
  def __init__(self):
    return
  
  def create(self, new_book:Book) -> CreateBookResponse:
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
          return CreateBookResponse()
    
    for review in new_book.reviews:
      book.reviews.append(Review(content=review.content, 
                                publication_date=review.publication_date))
    book.save()
    return CreateBookResponse(book)