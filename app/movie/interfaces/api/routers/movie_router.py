from typing import List, Optional, Dict

from fastapi import APIRouter, Depends, Query, Body

from app.dendencies import get_movie_repository
from app.movie.application.use_cases.create_movie import CreateMovie
from app.movie.application.use_cases.delete_movie import DeleteMovie
from app.movie.application.use_cases.get_all_movies import GetAllMovies
from app.movie.application.use_cases.get_movie_by_id import GetMovieById
from app.movie.application.use_cases.get_movie_by_title import GetMoviesByTitle
from app.movie.application.use_cases.update_movie import UpdateMovie, UpdateMovieParam
from app.movie.domain.repositories.movie_repository import MovieRepository
from app.movie.infrastructure.mappers.create_movie_schema_mapper import CreateMovieSchemaMapper
from app.movie.infrastructure.mappers.movie_schema_mapper import MovieSchemaMapper
from app.movie.infrastructure.mappers.update_movie_schema_mapper import UpdateMovieSchemaMapper
from app.movie.interfaces.api.schemas.create_movie import MovieCreateSchema
from app.movie.interfaces.api.schemas.movie_schema import MovieSchema
from app.movie.interfaces.api.schemas.movie_update import MovieUpdateSchema

router = APIRouter()


@router.get('/movies', response_model=List[MovieSchema])
def get_all_movies(repository: MovieRepository = Depends(get_movie_repository)) -> List[MovieSchema]:
    use_case = GetAllMovies(repository=repository)
    movies = use_case.execute()
    return [MovieSchemaMapper.map(movie) for movie in movies]


@router.get('/movies/{id_movie}', response_model=MovieSchema | Dict)
def get_movies_by_id(id_movie: int, repository: MovieRepository = Depends(get_movie_repository)) -> MovieSchema | Dict:
    use_case = GetMovieById(repository=repository)
    movie = use_case.execute(id_movie=id_movie)
    if movie is not None:
        return MovieSchemaMapper.map(movie)
    else:
        return {}


@router.get('/movies/', response_model=List[MovieSchema])
def get_movies_by_title(title: str, repository: MovieRepository = Depends(get_movie_repository)) -> List[MovieSchema]:
    use_case = GetMoviesByTitle(repository=repository)
    movies = use_case.execute(title=title)
    return [MovieSchemaMapper.map(movie) for movie in movies]


@router.post('/movies', response_model=MovieSchema | Dict)
def create_movie(movie: MovieCreateSchema = Body(),
                 repository: MovieRepository = Depends(get_movie_repository)) -> MovieSchema | Dict:
    use_case = CreateMovie(repository=repository)
    movie = use_case.execute(movie=CreateMovieSchemaMapper.reverseMap(movie))
    return MovieSchemaMapper.map(movie)


@router.put('/movies/{id_movie}', response_model=MovieSchema | Dict)
def update_movie(id_movie: int, movie: MovieUpdateSchema = Body(),
                 repository: MovieRepository = Depends(get_movie_repository)) -> MovieSchema | Dict:
    use_case = UpdateMovie(repository=repository)
    movie = use_case.execute(
        update=UpdateMovieParam(id_movie=id_movie, movie=UpdateMovieSchemaMapper.reverseMap(movie)))
    return MovieSchemaMapper.map(movie)


@router.delete('/movies/{id_movie}', response_model=bool)
def update_movie(id_movie: int,
                 repository: MovieRepository = Depends(get_movie_repository)) -> bool:
    use_case = DeleteMovie(repository=repository)
    return use_case.execute(id_movie=id_movie)
