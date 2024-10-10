from abc import ABC
from typing import List, Optional

from app.movie.domain.datasources.movie_data_source import MovieDataSource
from app.movie.domain.entities.movie import Movie
from app.movie.domain.repositories.movie_repository import MovieRepository


class MovieRepositoryImpl(MovieRepository, ABC):
    def __init__(self, data_source: MovieDataSource):
        self.data_source = data_source

    def get_all(self) -> List[Movie]:
        return self.data_source.get_all()

    def get_by_id(self, id_movie: int) -> Movie:
        return self.data_source.get_by_id(id_movie)

    def get_by_title(self, title: str) -> List[Movie]:
        return self.data_source.get_by_title(title)

    def create(self, movie: Movie) -> Movie:
        return self.data_source.create(movie)

    def update(self, id_movie: int, movie: Movie) -> Optional[Movie]:
        return self.data_source.update(id_movie,movie)

    def delete(self, id_movie: int) -> bool:
        return self.data_source.delete(id_movie)

