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

    async def get(self, url: str, token: str):
        header = {"Authorization": token}
        async with aiohttp.ClientSession(headers=header) as cs:
            async with cs.get(self.__base_url + url) as r:
                return Response(r.status, await r.json())