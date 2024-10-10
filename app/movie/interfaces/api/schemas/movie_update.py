from typing import Optional

from pydantic import BaseModel


class MovieUpdateSchema(BaseModel):
    title: Optional[str]
    director: Optional[str]
    year: Optional[int]
    gender: Optional[str]
