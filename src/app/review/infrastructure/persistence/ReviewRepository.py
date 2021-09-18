from typing import List, Optional
from src.app.review.domain.Review import Review
from src.app.review.domain.models.Review import Review as ReviewModel
from src.app.review.domain.IReviewRepository import IReviewRepository

class ReviewRepository(IReviewRepository):
  def __init__(self):
    pass

  def save(self, review: Review) -> Optional[Review]:
    new_review = ReviewModel(content=review.content,
                              publication_date=review.publication_date,
                              book_id=review.book_id)
    new_review.save()
    return new_review

  def get(self, review_id: int) -> Optional[Review]:
    return ReviewModel.get_by_id(review_id)

  def get_all(self) -> List[Review]:
    reviews = ReviewModel.get_all();
    return reviews
  
  def update(self, review: dict) -> Optional[Review]:
    review_to_update = ReviewModel.get_by_id(review["id"])
    if review_to_update is not None:
      for key in review.keys():
        if (key != "id"):
          try:
            setattr(review_to_update, key, review[key])
          except:
            return None
    else:
      return None
    review_to_update.save()
    return review_to_update

  def delete(self, review_id: int):
    review = ReviewModel.get_by_id(review_id)
    review.delete()