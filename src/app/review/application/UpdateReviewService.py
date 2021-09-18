from src.app.review.domain.IReviewRepository import IReviewRepository
from src.app.review.application.UpdateReviewResponse import UpdateReviewResponse

class UpdateReviewService():
  def __init__(self, repository:IReviewRepository):
    self.repository = repository
  
  def update(self, update_data:dict) -> UpdateReviewResponse:
    return UpdateReviewResponse(self.repository.update(update_data))