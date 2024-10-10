from fastapi import FastAPI

from app.movie.interfaces.api.routers.movie_router import router as movie_router

app = FastAPI()
app.title = "Mi Primera App con FastAPI"
app.version = "2.0.0"

app.include_router(movie_router, prefix='/api', tags=["Movies"])
