from flask_restful import Api
from flask import Blueprint
from flask_restful import Resource

class AuthorResources(Resource):
  def get(self, author_id:int):
    return {
      'id': author_id,
      'message': "This is the author controller get method"
    }

author_controller = Blueprint('authors', __name__)
api = Api(author_controller)

api.add_resource(AuthorResources, '/authors/<int:author_id>', endpoint='authors')