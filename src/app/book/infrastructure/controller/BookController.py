from flask_restful import Api
from flask import Blueprint
from flask_restful import Resource

class BookResources(Resource):
  def get(self, book_id:int):
    return {
      'id': book_id,
      'message': "This is the book controller get method"
    }

book_controller = Blueprint('books', __name__)
api = Api(book_controller)

api.add_resource(BookResources, '/books/<int:book_id>', endpoint='books')