from src.app.author.domain.models.Author import Author
from src.app.review.domain.models.Review import Review
from src.app.book.domain.models.Book import Book, BookSchema
from flask_restful import Api
from flask import Blueprint
from flask_restful import Resource
from flask import  request

book_schema = BookSchema()

class BookResources(Resource):
  def get(self, book_id:int):
    result = Book.get_by_id(book_id)
    if result is not None:
      book = book_schema.dump(result)
      return book, 200
    return 'Book not found', 404
  
  def put(self, book_id:int):
    updated_book = request.get_json()
    if book_id is not None:
      book_found:Book = Book.get_by_id(book_id)
      if book_found is not None:
        for key in updated_book.keys():
          try:
            setattr(book_found, key, updated_book[key])
          except:
            return f'The {key} property cannot be modified', 400
      else:
        return 'Book not found', 404
      book_found.save()
      response = book_schema.dump(book_found)
      return response, 200
    return 'You should provide a book id', 400
  
  def delete(self, book_id:int):
    book = Book.get_by_id(book_id)
    if book is not None:
      book.delete()
      return 'Book deleted', 200
    return 'Book not found', 404

class BookListResources(Resource):
  def get(self):
    result = Book.get_all()
    books = BookSchema().dump(result, many=True)
    return books, 200
  
  def post(self):
    data = request.get_json()
    new_book:Book = book_schema.load(data)
    book = Book(name=new_book.name,
                cover=new_book.cover,
                abstract=new_book.abstract,
                publication_date=new_book.publication_date,
                reviews=new_book.reviews)

    for author in new_book.authors:
      if author.id is None:
        book.authors.append(Author(author.name))
      else:
        author_found = author.get_by_id(author.id)
        if (author_found is not None):
          book.authors.append(author_found)
        else:
          return f'Author with id: {author.id} not found', 404
    
    for review in new_book.reviews:
      book.reviews.append(Review(content=review.content, 
                                publication_date=review.publication_date))
    book.save()
    response = book_schema.dump(book)
    return response, 201

book_controller = Blueprint('books', __name__)
api = Api(book_controller)

api.add_resource(BookListResources, '/books', endpoint='books_list_resource')
api.add_resource(BookResources, '/books/<int:book_id>', endpoint='books')