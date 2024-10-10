from abc import ABC

from app.core.utils.mapper import Mapper, T1, T2
from app.movie.domain.entities.movie import Movie
from app.movie.interfaces.api.schemas.create_movie import MovieCreateSchema


class CreateMovieSchemaMapper(Mapper[MovieCreateSchema, Movie], ABC):
    @staticmethod
    def map(value: Movie) -> MovieCreateSchema:
        return MovieCreateSchema(
            id=value.id,
            title=value.title,
            director=value.director,
            year=value.year,
            gender=value.gender
        )

    @staticmethod
    def reverseMap(value: MovieCreateSchema) -> Movie:
        return Movie(
            id=value.id,
            title=value.title,
            director=value.director,
            year=value.year,
            gender=value.gender
        )
