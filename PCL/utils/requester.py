from typing import Any
import aiohttp
from aiohttp.typedefs import StrOrURL
from attr import dataclass


@dataclass
class Response:
    status: int
    body: Any


class Requester:
    def __init__(self, base_url: StrOrURL, headers):
        self.base_url = base_url
        self.headers = headers

    async def request(self, method: str, url: StrOrURL, **kwargs: Any):
        async with aiohttp.ClientSession(headers=self.headers) as cs:
            async with cs.request(method, self.__base_url + url, **kwargs) as r:
                return Response(r.status, await r.json())

    async def get(self, url: StrOrURL, **kwargs: Any):
        return await self.request("GET", url, **kwargs)

    async def post(self, url: StrOrURL, **kwargs: Any):
        return await self.request("POST", url, **kwargs)