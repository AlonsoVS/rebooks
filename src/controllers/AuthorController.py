from src.persistence.models.Author import Author, AuthorSchema
from flask_restful import Api
from flask import Blueprint
from flask_restful import Resource
from flask import  request

author_schema = AuthorSchema()

class AuthorResources(Resource):
  def get(self, author_id:int):
    result = Author.get_by_id(author_id)
    if result is not None:
      author = author_schema.dump(result)
      return author, 200
    return 'Author not found', 404
  
  def put(self, author_id:int):
    updated_author = request.get_json()
    if author_id is not None:
      author_found:Author = Author.get_by_id(author_id)
      if author_found is not None:
        for key in updated_author.keys():
          try:
            setattr(author_found, key, updated_author[key])
          except:
            return f'The {key} property cannot be modified'
      else:
        return 'Author not found', 404
      author_found.save()
      response = author_schema.dump(author_found)
      return response, 200
    return 'You should provide an author id', 400
  
  def delete(self, author_id:int):
    author = Author.get_by_id(author_id)
    if author is not None:
      author.delete()
      return 'Author deleted', 200
    return 'Author not found', 404

class AuthorListResources(Resource):
  def get(self):
    authors = Author.get_all()
    result = author_schema.dump(authors, many=True)
    return result, 200
  
  def post(self):
    data = request.get_json()
    new_author:Author = author_schema.load(data)
    author = Author(name=new_author.name)
    author.save()
    response = author_schema.dump(author)
    return response, 201

author_controller = Blueprint('authors', __name__)
api = Api(author_controller)

api.add_resource(AuthorListResources, '/authors', endpoint='authors_list_resource')
api.add_resource(AuthorResources, '/authors/<int:author_id>', endpoint='authors')