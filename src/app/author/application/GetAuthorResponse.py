from typing import Optional
from src.app.author.domain.models.Author import Author
from src.app.author.domain.Author import AuthorSchema

class GetAuthorResponse():
  def __init__(self, author:Author):
    self.author = author
  
  def get_author(self) -> Optional[Author]:
    if (self.author is not None):
      return AuthorSchema().dump(self.author)
    return None