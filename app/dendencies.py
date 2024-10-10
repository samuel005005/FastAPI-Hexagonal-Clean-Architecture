from fastapi import Depends

from app.movie.domain.datasources.movie_data_source import MovieDataSource
from app.movie.domain.repositories.movie_repository import MovieRepository
from app.movie.infrastructure.datasource.movie_data_source_impl import MovieDataSourceImpl
from app.movie.infrastructure.repositories.movie_repository_impl import MovieRepositoryImpl


def get_movie_data_source() -> MovieDataSource:
    return MovieDataSourceImpl()


def get_movie_repository(data_source: MovieDataSource = Depends(get_movie_data_source)) -> MovieRepository:
    return MovieRepositoryImpl(data_source=data_source)


def get_movie_repository_manual() -> MovieRepository:
    data_source = get_movie_data_source()
    return MovieRepositoryImpl(data_source=data_source)
