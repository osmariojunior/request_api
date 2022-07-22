from src.domain.usecases import starships_list_colector
from .starships_list_colector import StarshipsListColector
from src.infra.swapi_api_consumer import SwapiApiConsumer

def test_list():
    api_consumer = SwapiApiConsumer()
    starships_list_colector = StarshipsListColector(api_consumer)

    page = 1
    starships_list_colector.list(page)
    