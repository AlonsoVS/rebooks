from src.app.author.domain.IAuthorRepository import IAuthorRepository
from src.app.author.application.DeleteAuthorResponse import DeleteAuthorResponse
from src.app.author.domain.models.Author import Author

class DeleteAuthorService():
  def __init__(self, repository:IAuthorRepository):
    self.repository = repository
  
  def delete(self, id:int) -> DeleteAuthorResponse:
    author_found = self.repository.get(id)
    if (author_found is None):
      return DeleteAuthorResponse(id, False)
    self.repository.delete(id)
    return DeleteAuthorResponse(id, True)