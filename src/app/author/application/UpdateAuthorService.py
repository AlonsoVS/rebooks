from src.app.author.domain.IAuthorRepository import IAuthorRepository
from src.app.author.application.UpdateAuthorResponse import UpdateAuthorResponse
from src.app.author.domain.models.Author import Author

class UpdateAuthorService():
  def __init__(self, repository:IAuthorRepository):
    self.repository = repository
  
  def update(self, update_data:dict) -> UpdateAuthorResponse:
    return UpdateAuthorResponse(self.repository.update(update_data))