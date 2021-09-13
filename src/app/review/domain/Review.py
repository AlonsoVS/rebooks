from src.app.book.domain.Book import Book
from datetime import date
from typing import List

class Review():
  id:int = None
  content:str = None
  publication_date:date = None
  book_id:int = None
  book:List[Book] = []
  
  def __init__(self, content:str, book_id:int=None, publication_date:date=None):
    self.content = content
    self.publication_date = publication_date
    self.book_id = book_id
  
  def __repr__(self):
    return f'Review:{self.__dict__}'