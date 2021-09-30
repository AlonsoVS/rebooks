from src.app.shared.auth.AuthTools import auth_token_required
from src.app.author.application.DeleteAuthorService import DeleteAuthorService
from src.app.author.application.UpdateAuthorService import UpdateAuthorService
from src.app.author.application.CreateAuthorService import CreateAuthorService
from src.app.author.application.GetAuthorsService import GetAuthorsService
from src.app.author.domain.Author import Author, AuthorSchema
from src.app.author.infrastructure.persistence.AuthorRepository import AuthorRepository
from flask_restful import Api
from flask import Blueprint
from flask_restful import Resource
from flask import  request

author_schema = AuthorSchema()
author_repository = AuthorRepository()
get_books_service = GetAuthorsService(author_repository)
create_author_service = CreateAuthorService(author_repository)
update_author_service = UpdateAuthorService(author_repository)
delete_author_service = DeleteAuthorService(author_repository)

class AuthorResources(Resource):
  @auth_token_required
  def get(self, author_id:int):
    result = get_books_service.find_by_id(author_id).get_author();
    if result is None:
      return 'Author not found', 404
    return result, 200
  
  @auth_token_required
  def delete(self, author_id:int):
    delete_response = delete_author_service.delete(author_id)
    if (delete_response.is_deleted()):
      return f'Deleted author with id: {delete_response.deleted_id()}', 200
    return 'Author not found', 404

class AuthorListResources(Resource):
  @auth_token_required
  def get(self):
    response = get_books_service.get_all()
    return response.get_authors(), 200
  
  @auth_token_required
  def post(self):
    data = request.get_json()
    new_author:Author = author_schema.load(data)
    create_response = create_author_service.create(new_author)
    author_created = create_response.created()
    if author_created:
      return author_created, 201
    return f'Error: Could not create the author', 400
  
  @auth_token_required
  def put(self):
    update_data = request.get_json()
    update_response = update_author_service.update(update_data)
    author_updated = update_response.updated()
    if author_updated:
      return author_updated, 200
    return f'Error: Could not update the author with id: {update_data["id"]}', 400

author_controller = Blueprint('authors', __name__)
api = Api(author_controller)

api.add_resource(AuthorListResources, '/authors', endpoint='authors_list_resource')
api.add_resource(AuthorResources, '/authors/<int:author_id>', endpoint='authors')