from typing import Any
import aiohttp
from attr import dataclass
from token import token


@dataclass
class Response:
    status: int
    body: Any


class Requester:
    __base_url = "https://discord.com/api/v8/"
    __token = token

    async def request(self, method: str, url: str, **kwargs: Any):
        async with aiohttp.ClientSession(headers={"Authorization": self.__token}) as cs:
            async with cs.request(method, self.__base_url + url, **kwargs) as r:
                return Response(r.status, await r.json())

    async def get(self, url: str, **kwargs: Any):
        return await self.request("GET", url, **kwargs)

    async def post(self, url: str, **kwargs: Any):
        return await self.request("POST", url, **kwargs)