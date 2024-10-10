from app.movie.infrastructure.models.movie_model import json_to_movie

moviesJson = [
    {
        "id": 1,
        "title": "El Padrino",
        "director": "Francis Ford Coppola",
        "year": 1972,
        "gender": "Crimen, Drama"
    },
    {
        "id": 2,
        "title": "El Señor de los Anillos: La Comunidad del Anillo",
        "director": "Peter Jackson",
        "year": 2001,
        "gender": "Fantasía, Aventura"
    },
    {
        "id": 3,
        "title": "Inception",
        "director": "Christopher Nolan",
        "year": 2010,
        "gender": "Ciencia Ficción, Acción"
    },
    {
        "id": 4,
        "title": "Matrix",
        "director": "Lana Wachowski, Lilly Wachowski",
        "year": 1999,
        "gender": "Ciencia Ficción, Acción"
    },
    {
        "id": 5,
        "title": "Pulp Fiction",
        "director": "Quentin Tarantino",
        "year": 1994,
        "gender": "Crimen, Drama"
    }
]

movies = [json_to_movie(movie) for movie in moviesJson]
