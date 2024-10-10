import datetime

from pydantic import BaseModel, Field


class MovieCreateSchema(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=20)
    director: str
    year: int = Field(le=datetime.date.today().year, ge=1900)
    gender: str

    model_config = {
        'json_schema_extra': {
            'example': {
                'id': 4,
                'title': 'Matrix',
                'director': 'Lana Wachowski, Lilly Wachowski',
                'year': 1999,
                'gender': 'Ciencia Ficción, Acción'
            }
        }
    }

# gt greater than
# ge greater than or equal
# lt less than
# le less than or equal
