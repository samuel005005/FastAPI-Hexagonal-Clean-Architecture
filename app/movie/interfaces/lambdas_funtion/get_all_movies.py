import json

from app.dendencies import get_movie_repository, get_movie_repository_manual
from app.movie.application.use_cases.get_all_movies import GetAllMovies
from app.movie.domain.repositories.movie_repository import MovieRepository
from app.movie.infrastructure.mappers.movie_schema_mapper import MovieSchemaMapper


def lambda_handler(event, context):
    body = json.loads(event['body'])

    order_id = body['order_id']
    items = body['items']
    # Crear el repositorio manualmente
    repository = get_movie_repository_manual()

    # Ejecutar el caso de uso
    use_case = GetAllMovies(repository=repository)
    movies = use_case.execute()

    # Mapear los resultados a DTOs usando MovieSchemaMapper
    return [MovieSchemaMapper.map(movie) for movie in movies]

