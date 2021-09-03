from src.persistence.models.Review import ReviewSchema
from flask_restful import Api
from flask import Blueprint
from flask_restful import Resource

class ReviewResources(Resource):
  def get(self, review_id:int):
    return {
      'id': review_id,
      'message': "This is the review get controller"
    }

review_controller = Blueprint('reviews', __name__)
api = Api(review_controller)

api.add_resource(ReviewResources, '/reviews/<int:review_id>', endpoint='reviews')