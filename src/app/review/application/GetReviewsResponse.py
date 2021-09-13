from src.app.review.domain.models.Review import Review
from src.app.review.domain.Review import ReviewSchema
from typing import List

class GetReviewsResponse():
  def __init__(self, reviews:List[Review]):
    self.reviews = reviews
  
  def get_reviews(self) -> List[Review]:
    return ReviewSchema().dump(self.reviews, many=True)
