from src.app.author.application.GetAuthorResponse import GetAuthorResponse
from src.app.author.application.GetAuthorsResponse import GetAuthorsResponse
from src.app.author.domain.models.Author import Author

class GetAuthorsService():
  
  def __init__(self):
    return

  def get_all(self) -> GetAuthorsResponse:
    return GetAuthorsResponse(Author.get_all())
  
  def find_by_id(self, id:int) -> GetAuthorResponse:
    return GetAuthorResponse(Author.get_by_id(id))