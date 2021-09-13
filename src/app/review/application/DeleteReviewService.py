from src.app.review.application.DeleteReviewResponse import DeleteReviewResponse
from src.app.review.domain.models.Review import Review

class DeleteReviewService():
  def __init__(self):
    return
  
  def delete(self, id:int) -> DeleteReviewResponse:
    review_found = Review.get_by_id(id)
    if (review_found is None):
      return DeleteReviewResponse(id, False)
    review_found.delete()
    return DeleteReviewResponse(id, True)