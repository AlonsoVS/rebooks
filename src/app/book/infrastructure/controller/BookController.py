from src.app.book.application.UpdateBookService import UpdateBookService
from src.app.book.application.CreateBookService import CreateBookService
from src.app.book.application.DeleteBookService import DeleteBookService
from src.app.book.application.GetBooksService import GetBooksService
from src.app.book.domain.Book import Book, BookSchema
from flask_restful import Api
from flask import Blueprint
from flask_restful import Resource
from flask import request

book_schema = BookSchema()
get_books_service = GetBooksService()
delete_book_service = DeleteBookService()
create_book_service = CreateBookService()
update_book_service = UpdateBookService()

class BookResources(Resource):
  def get(self, book_id:int):
    result = get_books_service.find_by_id(book_id).get_book()
    if result is None:
      return 'Book not found', 404
    return result, 200
  
  def put(self, book_id:int):
    update_data = request.get_json()
    update_response = update_book_service.update(book_id, update_data)
    book_updated = update_response.updated()
    if book_updated:
      return book_updated, 200
    return f'Error: Could not update the book with id: {book_id}', 400
    
  def delete(self, book_id:int):
    delete_response = delete_book_service.delete(book_id)
    if (delete_response.is_deleted()):
      return f'Deleted book with id: {delete_response.deleted_id()}', 200
    return 'Book not found', 404

class BookListResources(Resource):
  def get(self):
    response = get_books_service.get_all()
    return response.get_books(), 200
  
  def post(self):
    data = request.get_json()
    new_book:Book = book_schema.load(data)
    create_response = create_book_service.create(new_book)
    book_created = create_response.created()
    if book_created:
      return book_created, 201
    return f'Error: Could not create the book', 400

book_controller = Blueprint('books', __name__)
api = Api(book_controller)

api.add_resource(BookListResources, '/books', endpoint='books_list_resource')
api.add_resource(BookResources, '/books/<int:book_id>', endpoint='books')