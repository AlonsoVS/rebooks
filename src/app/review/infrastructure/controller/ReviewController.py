from src.app.review.domain.models.Review import Review, ReviewSchema
from flask_restful import Api
from flask import Blueprint
from flask_restful import Resource
from flask import  request

review_schema = ReviewSchema()

class ReviewResources(Resource):
  def get(self, review_id:int):
    result = Review.get_by_id(review_id)
    if result is not None:
      review = review_schema.dump(result)
      return review, 200
    return 'Review not found', 404
  
  def put(self, review_id:int):
    updated_review = request.get_json()
    if id is not None:
      review_found:Review = Review.get_by_id(review_id)
      if review_found is not None:
        for key in updated_review.keys():
          try:
            setattr(review_found, key, updated_review[key])
          except:
            return f'The {key} property cannot be modified'
      else:
        return 'Review not found', 404
      review_found.save()
      response = review_schema.dump(review_found)
      return response, 200
    return 'You should provide a review id', 400
  
  def delete(self, review_id:int):
    review = Review.get_by_id(review_id)
    if review is not None:
      review.delete()
      return 'Review deleted', 200
    return 'Review not found', 404

class ReviewListResources(Resource):
  def get(self):
    result = Review.get_all()
    reviews = review_schema.dump(result, many=True)
    return reviews, 200
  
  def post(self):
    data = request.get_json()
    new_review:Review = review_schema.load(data)
    review = Review(content=new_review.content,
                    publication_date=new_review.publication_date,
                    book_id=new_review.book_id)
    review.save()
    response = review_schema.dump(review)
    return response, 201

review_controller = Blueprint('reviews', __name__)
api = Api(review_controller)

api.add_resource(ReviewListResources, '/reviews', endpoint='reviews_list_resource')
api.add_resource(ReviewResources, '/reviews/<int:review_id>', endpoint='reviews')