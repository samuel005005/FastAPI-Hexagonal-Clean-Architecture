# Definimos la clase movie
class MovieModel:
    def __init__(self, id_movie: int, title: str, director: str, year: int, gender: str):
        self.id_movie = id_movie
        self.title = title
        self.director = director
        self.year = year
        self.gender = gender

    def __repr__(self):
        return f"Movie(id={self.id_movie}, title='{self.title}', director='{self.director}', year={self.year}, gender='{self.gender}')"


def json_to_movie(movie_json: dict) -> MovieModel:
    return MovieModel(
        id_movie=movie_json["id"],
        title=movie_json["title"],
        director=movie_json["director"],
        year=movie_json["year"],
        gender=movie_json["gender"]
    )
