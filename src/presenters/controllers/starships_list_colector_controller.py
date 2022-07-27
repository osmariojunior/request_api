from src.domain.usecases.starships_list_colector import StarshipsListColectorInteface
from typing import Dict, Type


class StarshipsListColectorController:
    '''Controller to list starships'''

    def __init__(self, starships_list_colector: Type[StarshipsListColectorInteface]) -> None:
        self.__use_case = starships_list_colector

    def handle(self, http_request: Dict) -> Dict:
        '''Handler to list colector'''

        page = http_request["query_params"]["page"]
        starships_list = self.__use_case.list(page)
        http_response = {"status_code": 200, "data": starships_list }

        return http_response
        
