from flask_restful import Api, Resource
from flask import Blueprint

class MainController(Resource):
  def get(self):
    return "<h1>Hello. Welcome to ReBooks 😊.</h1>", 200

main_controller = Blueprint('main', __name__)
api = Api(main_controller)

api.add_resource(MainController, '/main', '/', endpoint='main')