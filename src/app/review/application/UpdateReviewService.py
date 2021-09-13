from src.app.review.application.UpdateReviewResponse import UpdateReviewResponse
from src.app.review.domain.models.Review import Review

class UpdateReviewService():
  def __init__(self):
    return
  
  def update(self, review_id:int, update_data:dict) -> UpdateReviewResponse:
    if review_id is not None:
      review_to_update:Review = Review.get_by_id(review_id)
      if review_to_update is not None:
        for key in update_data.keys():
          try:
            setattr(review_to_update, key, update_data[key])
          except:
            return UpdateReviewResponse()
      else:
        return UpdateReviewResponse()
      review_to_update.save()
      return UpdateReviewResponse(review_to_update)
    return UpdateReviewResponse()