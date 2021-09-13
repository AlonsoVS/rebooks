from src.app.author.application.UpdateAuthorResponse import UpdateAuthorResponse
from src.app.author.domain.models.Author import Author

class UpdateAuthorService():
  def __init__(self):
    return
  
  def update(self, author_id:int, update_data:dict) -> UpdateAuthorResponse:
    if author_id is not None:
      author_to_update:Author = Author.get_by_id(author_id)
      if author_to_update is not None:
        for key in update_data.keys():
          try:
            setattr(author_to_update, key, update_data[key])
          except:
            return UpdateAuthorResponse()
      else:
        return UpdateAuthorResponse()
      author_to_update.save()
      return UpdateAuthorResponse(author_to_update)
    return UpdateAuthorResponse()