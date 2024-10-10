from typing import List

from app.core.utils.use_case_arguments import UseCaseArgument
from app.core.utils.use_case_no_arguments import UseCaseNoArgument, Type
from app.movie.domain.entities.movie import Movie
from app.movie.domain.repositories.movie_repository import MovieRepository


class GetMovieById(UseCaseArgument[int, Movie]):
    def __init__(self, repository: MovieRepository):
        self.repository = repository

    def execute(self, id_movie: int) -> Movie:
        return self.repository.get_by_id(id_movie)
