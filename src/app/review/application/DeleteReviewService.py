from src.app.review.domain.IReviewRepository import IReviewRepository
from src.app.review.application.DeleteReviewResponse import DeleteReviewResponse

class DeleteReviewService():
  def __init__(self, repository:IReviewRepository):
    self.repository = repository
  
  def delete(self, id:int) -> DeleteReviewResponse:
    review_found = self.repository.get(id)
    if (review_found is None):
      return DeleteReviewResponse(id, False)
    self.repository.delete(id)
    return DeleteReviewResponse(id, True)