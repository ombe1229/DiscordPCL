from PCL.discord_client import DiscordRequester
import asyncio
from debug import token


async def init():
    requester = DiscordRequester(token)
    guilds = [guild async for guild in requester.get_user_guilds()]
    print(len(guilds))
    print(guilds)


asyncio.run(init())

# Python: 267624335836053506
