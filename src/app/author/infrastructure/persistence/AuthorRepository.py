from typing import List, Optional
from src.app.author.domain.Author import Author
from src.app.author.domain.models.Author import Author as AuthorModel
from src.app.author.domain.IAuthorRepository import IAuthorRepository

class AuthorRepository(IAuthorRepository):
  def __init__(self):
    pass

  def save(self, author:Author) -> Optional[Author]:
    new_author = AuthorModel(name=author.name, books=author.books)
    new_author.save()
    return new_author

  def get(self, author_id: int) -> Optional[Author]:
    return AuthorModel.get_by_id(author_id)

  def get_all(self) -> List[Author]:
    authors = AuthorModel.get_all();
    return authors
  
  def update(self, author:dict) -> Optional[Author]:
    author_to_update = AuthorModel.get_by_id(author["id"])
    if author_to_update is not None:
      for key in author.keys():
        if (key != "id"):
          try:
            setattr(author_to_update, key, author[key])
          except:
            return None
    else:
      return None
    author_to_update.save()
    return author_to_update

  def delete(self, author_id: int):
    author = AuthorModel.get_by_id(author_id)
    author.delete()