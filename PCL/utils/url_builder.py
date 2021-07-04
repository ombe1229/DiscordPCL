from typing import Optional
from urllib.parse import urlencode


class UrlBuilder:
    def __init__(self):
        self.__path: str = ""
        self.__query_params: dict[str, Optional[str]] = {}

    @staticmethod
    def isNullOrWhiteSpace(str: str = None):
        return not str or str.isspace()

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def query_params(self):
        return self.__query_params

    @query_params.setter
    def query_params(self, key: str, value: Optional[str] = None):
        encoded_key = urlencode(key)
        encoded_value = urlencode(value)
        self.__query_params[encoded_key] = encoded_value
    
    def build(self):
        buffer = 
