from abc import ABC

from app.core.utils.mapper import Mapper, T1, T2
from app.movie.domain.entities.movie import Movie
from app.movie.interfaces.api.schemas.movie_update import MovieUpdateSchema


class UpdateMovieSchemaMapper(Mapper[MovieUpdateSchema, Movie], ABC):
    @staticmethod
    def map(value: Movie) -> MovieUpdateSchema:
        return MovieUpdateSchema(
            id=value.id,
            title=value.title,
            director=value.director,
            year=value.year,
            gender=value.gender
        )

    @staticmethod
    def reverseMap(value: MovieUpdateSchema) -> Movie:
        return Movie(
            id=0,
            title=value.title,
            director=value.director,
            year=value.year,
            gender=value.gender
        )
