from src.app.shared.auth.AuthTools import auth_token_required
from src.app.user.application.UpdateUserService import UpdateUserService
from src.app.user.infrastructure.persistence.UserRepository import UserRepository
from src.app.user.domain.User import UserSchema
from src.app.user.application.DeleteUserService import DeleteUserService
from src.app.user.application.CreateUserService import CreateUserService
from src.app.user.application.GetUsersService import GetUsersService
from flask_restful import Api
from flask import Blueprint
from flask_restful import Resource
from flask import request

user_repository = UserRepository()
get_user_service = GetUsersService(user_repository)
create_user_service = CreateUserService(user_repository)
update_user_service = UpdateUserService(user_repository)
delete_user_service = DeleteUserService(user_repository)

class UserListResources(Resource):
  @auth_token_required
  def get(self):
    result = get_user_service.get_all()
    return UserSchema().dump(result.get_users(), many=True), 200
  
  def post(self):
    data = request.get_json()
    create_response = create_user_service.create(data)
    user_created = create_response.created()
    if (user_created):
      return user_created, 201
    return f'Error: Could not create the user', 400
  
  @auth_token_required
  def put(self):
    update_data = request.get_json()
    update_response = update_user_service.update(update_data)
    user_updated = update_response.updated()
    if user_updated:
      return user_updated, 200
    return f'Error: Could not update the user with id: {update_data["id"]}', 400

class UserResource(Resource):
  @auth_token_required
  def get(self, user_id:int):
    result = get_user_service.find_by_id(user_id).get_user();
    if result is None:
      return 'User not found', 404
    return result, 200

  @auth_token_required
  def delete(self, user_id:int):
    delete_response = delete_user_service.delete(user_id)
    if (delete_response.is_deleted()):
      return f'User with id = {user_id} deleted!', 200
    return 'User not found!', 200
  

user_controller = Blueprint('users', __name__)
api = Api(user_controller)

api.add_resource(UserListResources, '/users', endpoint='user_list_resource')
api.add_resource(UserResource, '/users/<int:user_id>', endpoint='user_resource')