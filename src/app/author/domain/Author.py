from typing import List

class Author():
  id:int = None
  name:str = None
  books = []

  def __init__(self, name:str, id:int=None, books:List=[]):
    self.id = id
    self.name = name
    self.books = books
  
  def __repr__(self):
    return f'Author:{self.__dict__}'