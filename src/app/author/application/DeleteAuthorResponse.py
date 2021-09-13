class DeleteAuthorResponse():
  def __init__(self, author_id:int, deleted:bool):
    self.author_id = author_id
    self.deleted = deleted
  
  def is_deleted(self):
    return self.deleted
  
  def deleted_id(self):
    return self.author_id