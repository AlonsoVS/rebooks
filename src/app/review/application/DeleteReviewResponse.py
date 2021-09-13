class DeleteReviewResponse():
  def __init__(self, review_id:int, deleted:bool):
    self.review_id = review_id
    self.deleted = deleted
  
  def is_deleted(self):
    return self.deleted
  
  def deleted_id(self):
    return self.review_id