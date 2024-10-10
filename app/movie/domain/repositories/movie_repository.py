from abc import ABC, abstractmethod
from typing import List, Optional

from app.movie.domain.entities.movie import Movie


class MovieRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Movie]:
        pass

    @abstractmethod
    def get_by_id(self, id_movie: int) -> Movie:
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> List[Movie]:
        pass

    @abstractmethod
    def create(self, movie: Movie) -> Movie:
        pass

    @abstractmethod
    def update(self, id_movie: int, movie: Movie) -> Optional[Movie]:
        pass

    @abstractmethod
    def delete(self, id_movie: int) -> bool:
        pass
