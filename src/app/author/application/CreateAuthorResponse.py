from typing import Optional
from src.app.author.domain.models.Author import Author
from src.app.author.domain.Author import AuthorSchema

class CreateAuthorResponse():
  def __init__(self, author:Optional[Author]=None):
    self.author = author
  
  def created(self):
    if (self.author is None):
      return False
    return AuthorSchema().dump(self.author)