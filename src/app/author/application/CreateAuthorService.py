from src.app.author.domain.IAuthorRepository import IAuthorRepository
from src.app.author.application.CreateAuthorResponse import CreateAuthorResponse
from src.app.author.domain.Author import Author

class CreateAuthorService():
  def __init__(self, repository:IAuthorRepository):
    self.repository = repository
  
  def create(self, new_author:Author) -> CreateAuthorResponse:
    return CreateAuthorResponse(self.repository.save(new_author))