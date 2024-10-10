from abc import ABC

from app.core.utils.mapper import Mapper, T1, T2
from app.movie.domain.entities.movie import Movie
from app.movie.infrastructure.models.movie_model import MovieModel
from app.movie.interfaces.api.schemas.movie_schema import MovieSchema


class MovieSchemaMapper(Mapper[MovieSchema, Movie], ABC):
    @staticmethod
    def map(value: Movie) -> MovieSchema:
        return MovieSchema(
            id=value.id,
            title=value.title,
            director=value.director,
            year=value.year,
            gender=value.gender
        )

    @staticmethod
    def reverseMap(value: MovieSchema) -> Movie:
        return Movie(
            id=value.id,
            title=value.title,
            director=value.director,
            year=value.year,
            gender=value.gender
        )
