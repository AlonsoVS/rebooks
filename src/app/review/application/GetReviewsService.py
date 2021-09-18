from src.app.review.application.GetReviewResponse import GetReviewResponse
from src.app.review.application.GetReviewsResponse import GetReviewsResponse
from src.app.review.domain.IReviewRepository import IReviewRepository

class GetReviewsService():
  def __init__(self, repository: IReviewRepository):
    self.repository = repository

  def get_all(self) -> GetReviewsResponse:
    return GetReviewsResponse(self.repository.get_all())
  
  def find_by_id(self, id:int) -> GetReviewResponse:
    return GetReviewResponse(self.repository.get(id))