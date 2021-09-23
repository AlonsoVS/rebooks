from src.app.author.application.GetAuthorResponse import GetAuthorResponse
from src.app.author.application.GetAuthorsResponse import GetAuthorsResponse
from src.app.author.domain.IAuthorRepository import IAuthorRepository

class GetAuthorsService():
  
  def __init__(self, repository:IAuthorRepository):
    self.repository = repository

  def get_all(self) -> GetAuthorsResponse:
    return GetAuthorsResponse(self.repository.get_all())
  
  def find_by_id(self, id:int) -> GetAuthorResponse:
    return GetAuthorResponse(self.repository.get(id))