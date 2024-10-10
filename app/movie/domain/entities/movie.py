class Movie:
    id: int
    title: str
    director: str
    year: int
    gender: str

    def __init__(self, id: int, title: str, director: str, year: int, gender: str):
        self.id = id
        self.title = title
        self.director = director
        self.year = year
        self.gender = gender
