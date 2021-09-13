from typing import Optional
from src.app.review.domain.models.Review import Review
from src.app.review.domain.Review import ReviewSchema

class CreateReviewResponse():
  def __init__(self, review:Optional[Review]=None):
    self.review = review
  
  def created(self):
    if (self.review is None):
      return False
    return ReviewSchema().dump(self.review)