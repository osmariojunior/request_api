from fastapi import APIRouter, Request


starships_router = APIRouter()


@starships_router.get('/api/starships/list')
def get_starships_in_pagination(request: Request):
    return {"msg": "ola"}