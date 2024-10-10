from abc import ABC

from app.core.utils.mapper import Mapper, T1, T2
from app.movie.domain.entities.movie import Movie
from app.movie.infrastructure.models.movie_model import MovieModel


class MovieModelMapper(Mapper[Movie, MovieModel], ABC):
    @staticmethod
    def map(value: MovieModel) -> Movie:
        return Movie(
            id=value.id_movie,
            title=value.title,
            director=value.director,
            year=value.year,
            gender=value.gender
        )

    @staticmethod
    def reverseMap(value: Movie) -> MovieModel:
        return MovieModel(
            id_movie=value.id,
            title=value.title,
            director=value.director,
            year=value.year,
            gender=value.gender
        )
