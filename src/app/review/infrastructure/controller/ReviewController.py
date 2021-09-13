from src.app.review.application.UpdateReviewService import UpdateReviewService
from src.app.review.application.DeleteReviewService import DeleteReviewService
from src.app.review.application.CreateReviewService import CreateReviewService
from src.app.review.application.GetReviewsService import GetReviewsService
from src.app.review.domain.Review import Review, ReviewSchema
from flask_restful import Api
from flask import Blueprint
from flask_restful import Resource
from flask import  request

review_schema = ReviewSchema()
get_reviews_service = GetReviewsService()
create_review_service = CreateReviewService()
delete_review_service = DeleteReviewService()
update_review_service = UpdateReviewService()

class ReviewResources(Resource):
  def get(self, review_id:int):
    result = get_reviews_service.find_by_id(review_id).get_review()
    if result is None:
      return 'Review not found', 404
    return result, 200

  def put(self, review_id:int):
    update_data = request.get_json()
    update_response = update_review_service.update(review_id, update_data)
    review_updated = update_response.updated()
    if review_updated:
      return review_updated, 200
    return f'Error: Could not update the review with id: {review_id}', 400

  def delete(self, review_id:int):
    delete_response = delete_review_service.delete(review_id)
    if (delete_response.is_deleted()):
      return f'Deleted review with id: {delete_response.deleted_id()}', 200
    return 'Review not found', 404

class ReviewListResources(Resource):
  def get(self):
    response = get_reviews_service.get_all()
    return response.get_reviews(), 200
  
  def post(self):
    data = request.get_json()
    new_review:Review = review_schema.load(data)
    create_response = create_review_service.create(new_review)
    review_created = create_response.created()
    if review_created:
      return review_created, 201
    return f'Error: Could not create the review', 400

review_controller = Blueprint('reviews', __name__)
api = Api(review_controller)

api.add_resource(ReviewListResources, '/reviews', endpoint='reviews_list_resource')
api.add_resource(ReviewResources, '/reviews/<int:review_id>', endpoint='reviews')