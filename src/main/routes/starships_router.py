from fastapi import APIRouter, Request
from src.validators.get_starships_in_pagination_validator import get_pagination_validator


starships_router = APIRouter()


@starships_router.get('/api/starships/list')
def get_starships_in_pagination(request: Request):


    get_pagination_validator(request)

    return {"msg": "ola"}