from typing import List, Optional
from src.app.review.domain.Review import Review
from abc import ABCMeta, abstractmethod

class IReviewRepository(metaclass=ABCMeta):
  @abstractmethod
  def save(self, review:Review) -> Optional[Review]:
    pass
  
  @abstractmethod
  def get(self, review_id:int) -> Optional[Review]:
    pass

  @abstractmethod
  def get_all(self) -> List[Review]:
    pass
  
  @abstractmethod
  def update(self, review:Review) -> Optional[Review]:
    pass

  @abstractmethod
  def delete(self, review_id:int):
    pass 