from src.app.shared.auth.AuthTools import auth_token_required
from src.app.book.application.UpdateBookService import UpdateBookService
from src.app.book.application.CreateBookService import CreateBookService
from src.app.book.application.DeleteBookService import DeleteBookService
from src.app.book.application.GetBooksService import GetBooksService
from src.app.book.domain.Book import Book, BookSchema
from src.app.book.infrastructure.persistence.BookRepository import BookRepository
from flask_restful import Api
from flask import Blueprint
from flask_restful import Resource
from flask import request

book_schema = BookSchema()
book_repository = BookRepository()
get_books_service = GetBooksService(book_repository)
delete_book_service = DeleteBookService(book_repository)
create_book_service = CreateBookService(book_repository)
update_book_service = UpdateBookService(book_repository)

class BookResources(Resource):
  @auth_token_required
  def get(self, book_id:int, *args, **kwargs):
    result = get_books_service.find_by_id(book_id).get_book()
    if result is None:
      return 'Book not found', 404
    return result, 200

  @auth_token_required  
  def delete(self, book_id:int, *args, **kwargs):
    delete_response = delete_book_service.delete(book_id)
    if (delete_response.is_deleted()):
      return f'Deleted book with id: {delete_response.deleted_id()}', 200
    return 'Book not found', 404

class BookListResources(Resource):
  @auth_token_required
  def get(self, *args, **kwargs):
    response = get_books_service.get_all()
    return response.get_books(), 200
  
  @auth_token_required
  def post(self, *args, **kwargs):
    data = request.get_json()
    new_book:Book = book_schema.load(data)
    create_response = create_book_service.create(new_book)
    book_created = create_response.created()
    if book_created:
      return book_created, 201
    return f'Error: Could not create the book', 400
  
  @auth_token_required
  def put(self, *args, **kwargs):
    update_data = request.get_json()
    update_response = update_book_service.update(update_data)
    book_updated = update_response.updated()
    if book_updated:
      return book_updated, 200
    return f'Error: Could not update the book with id: {update_data["id"]}', 400

book_controller = Blueprint('books', __name__)
api = Api(book_controller)

api.add_resource(BookListResources, '/books', endpoint='books_list_resource')
api.add_resource(BookResources, '/books/<int:book_id>', endpoint='books')