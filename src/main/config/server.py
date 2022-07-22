from fastapi import FastAPI
from src.main.routes import starships_router


app = FastAPI()

app.include_router(starships_router)