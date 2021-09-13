from src.app.author.domain.models.Author import Author
from src.app.author.domain.Author import AuthorSchema
from typing import List

class GetAuthorsResponse():
  def __init__(self, authors:List[Author]):
    self.authors = authors
  
  def get_authors(self) -> List[Author]:
    return AuthorSchema().dump(self.authors, many=True)
