from typing import Optional
from src.app.review.domain.models.Review import Review
from src.app.review.domain.Review import ReviewSchema

class UpdateReviewResponse():
  def __init__(self, review:Optional[Review]=None):
    self.review = review
  
  def updated(self):
    if (self.review is None):
      return False
    return ReviewSchema().dump(self.review)