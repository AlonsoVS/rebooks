class DeleteUserResponse():
  def __init__(self, user_id:int, deleted:bool):
    self.user_id = user_id
    self.deleted = deleted
  
  def is_deleted(self):
    return self.deleted
  
  def deleted_id(self):
    return self.user_id