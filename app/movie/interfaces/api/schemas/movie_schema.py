from pydantic import BaseModel


class MovieSchema(BaseModel):
    id: int
    title: str
    director: str
    year: int
    gender: str
