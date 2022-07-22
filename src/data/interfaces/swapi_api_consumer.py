from typing import Dict, Tuple, Type
from abc import ABC, abstractmethod
from requests import Request


class SwapiApiConsumerInterface(ABC):
    '''Api Consumer Interface'''

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        '''must implement'''
        raise Exception('Must implement get_starships')