from abc import ABC
from typing import List, Optional, Dict

from app.movie.domain.datasources.movie_data_source import MovieDataSource
from app.movie.domain.entities.movie import Movie
from app.movie.infrastructure.data.movies_data import movies
from app.movie.infrastructure.mappers.movie_model_mapper import MovieModelMapper
from app.movie.infrastructure.models.movie_model import MovieModel


class MovieDataSourceImpl(MovieDataSource, ABC):

    def get_all(self) -> List[Movie]:
        return [MovieModelMapper.map(value=movieModel) for movieModel in movies]

    def get_by_id(self, id_movie: int) -> Movie:
        movie = next((movie for movie in movies if movie.id_movie == id_movie), None)
        mapped_movie = MovieModelMapper.map(movie) if movie is not None else None
        return mapped_movie

    def get_by_title(self, title: str) -> Optional[List[Movie]]:
        return [next((MovieModelMapper.map(movie) for movie in movies if title in movie.title), None)]

    def create(self, movie: Movie) -> Movie:
        movies.append(MovieModelMapper.reverseMap(movie))
        return movie

    def update(self, id_movie: int, movie: Movie) -> Optional[Movie]:
        movie_to: MovieModel = next((movie for movie in movies if movie.id_movie == id_movie), None)
        if movie_to:
            if movie.title:
                movie_to.title = movie.title
            if movie.director:
                movie_to.director = movie.director
            if movie.year:
                movie_to.year = movie.year
            if movie.gender:
                movie_to.gender = movie.gender

        return MovieModelMapper.map(movie_to)

    def delete(self, id_movie: int) -> bool:
        movie_to_remove = next((movie for movie in movies if movie.id_movie == id_movie), None)
        if movie_to_remove:
            movies.remove(movie_to_remove)

        return True
