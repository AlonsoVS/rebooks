from src.app.author.application.CreateAuthorResponse import CreateAuthorResponse
from src.app.review.domain.models.Review import Review
from src.app.author.domain.models.Author import Author as AuthorModel
from src.app.author.domain.Author import Author

class CreateAuthorService():
  def __init__(self):
    return
  
  def create(self, new_author:Author) -> CreateAuthorResponse:
    author = AuthorModel(name=new_author.name)
    author.save()
    return CreateAuthorResponse(author)