from typing import Dict, Tuple, Type
from collections import namedtuple
import requests
from requests import Request
from src.errors.http_request_error import HttpRequestError
from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface


class SwapiApiConsumer(SwapiApiConsumerInterface):
    '''class to consume swapi api with http requests'''

    def __init__(self) -> None:
        self.get_starships_response = namedtuple('GET_Starships', 'status_code request response')
        self.get_starships_information_response = namedtuple('GET_Starships_Info', 'status_code request response')


    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        '''request starships pagination'''

        req = requests.Request(
            method='GET',
            url='https://swapi.dev/api/starships/',
            params={'page': page}
        )
        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared)
        status_code = response.status_code

        if (status_code >=200) and (status_code <=299):
            return self.get_starships_response(
                status_code=status_code, request=req, response=response.json()
            )
        else:
            raise HttpRequestError(
                message=response.json()["detail"], status_code=status_code
            )

    def get_starships_information(self, starship_id: int) -> Tuple[int, Type[Request], Dict]:
        '''request starships pagination'''

        req = requests.Request(
            method='GET',
            url=f'https://swapi.dev/api/starships/{starship_id}/',
        )
        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared)
        status_code = response.status_code

        if (status_code >=200) and (status_code <=299):
            return self.get_starships_information_response(
                status_code=status_code, request=req, response=response.json()
            )
        else:
            raise HttpRequestError(
                message=response.json()["detail"], status_code=status_code
            )

    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> any:
        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response