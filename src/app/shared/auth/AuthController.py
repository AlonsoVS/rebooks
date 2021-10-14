from src.app.user.infrastructure.persistence.UserRepository import UserRepository
from src.app.shared.auth.AuthTools import auth_token_required, create_token
from flask_restful import Api
from flask import Blueprint
from flask_restful import Resource
from flask import request

user_repository = UserRepository()

class AuthResource(Resource):
  def post(self):
    login_data = request.get_json()
    if (login_data):
      username = login_data["username"]
      password = login_data["password"]
      token = create_token(username, password)
      if (token):
        return {"token": token}, 200
      return "Authentication data is invalid!", 400
    return "Login data spected!", 200

auth_controller = Blueprint('authentication', __name__)
api = Api(auth_controller)

api.add_resource(AuthResource, '/auth', endpoint='auth_resource')