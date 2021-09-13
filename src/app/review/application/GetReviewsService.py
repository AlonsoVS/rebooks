from src.app.review.application.GetReviewResponse import GetReviewResponse
from src.app.review.application.GetReviewsResponse import GetReviewsResponse
from src.app.review.domain.models.Review import Review

class GetReviewsService():
  def __init__(self):
    return

  def get_all(self) -> GetReviewsResponse:
    return GetReviewsResponse(Review.get_all())
  
  def find_by_id(self, id:int) -> GetReviewResponse:
    return GetReviewResponse(Review.get_by_id(id))