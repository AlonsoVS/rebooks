from src.app.review.application.CreateReviewResponse import CreateReviewResponse
from src.app.review.domain.Review import Review
from src.app.review.domain.IReviewRepository import IReviewRepository

class CreateReviewService():
  def __init__(self, repository:IReviewRepository):
    self.repository = repository
  
  def create(self, new_review:Review) -> CreateReviewResponse:
    return CreateReviewResponse(self.repository.save(new_review))