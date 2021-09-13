from src.app.review.application.CreateReviewResponse import CreateReviewResponse
from src.app.review.domain.models.Review import Review as ReviewModel
from src.app.review.domain.Review import Review

class CreateReviewService():
  def __init__(self):
    return
  
  def create(self, new_review:Review) -> CreateReviewResponse:
    review = ReviewModel(content=new_review.content,
                        publication_date=new_review.publication_date,
                        book_id=new_review.book_id)
    review.save()
    return CreateReviewResponse(review)