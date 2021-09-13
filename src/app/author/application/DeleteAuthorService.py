from src.app.author.application.DeleteAuthorResponse import DeleteAuthorResponse
from src.app.author.domain.models.Author import Author

class DeleteAuthorService():
  def __init__(self):
    return
  
  def delete(self, id:int) -> DeleteAuthorResponse:
    author_found = Author.get_by_id(id)
    if (author_found is None):
      return DeleteAuthorResponse(id, False)
    author_found.delete()
    return DeleteAuthorResponse(id, True)