from typing import Dict, List, Type
from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface
from src.domain.usecases import StarshipsListColectorInteface
from src.infra.swapi_api_consumer import SwapiApiConsumer

class StarshipsListColector(StarshipsListColectorInteface):
    ''' Starships colector usecase'''

    def __init__(self, api_consumer: Type[SwapiApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer


    def list(self, page: int) -> List[Dict]:
        response = self.__api_consumer.get_starships(page)
        print(response)
