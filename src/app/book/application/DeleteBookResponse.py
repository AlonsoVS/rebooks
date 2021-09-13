class DeleteBookResponse():
  def __init__(self, book_id:int, deleted:bool):
    self.book_id = book_id
    self.deleted = deleted
  
  def is_deleted(self):
    return self.deleted
  
  def deleted_id(self):
    return self.book_id