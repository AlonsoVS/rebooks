from typing import Optional
from src.app.review.domain.models.Review import Review
from src.app.review.domain.Review import ReviewSchema

class GetReviewResponse():
  def __init__(self, review:Review):
    self.review = review
  
  def get_review(self) -> Optional[Review]:
    if (self.review is not None):
      return ReviewSchema().dump(self.review)
    return None