from PCL.utils.objects import Channel
from typing import List
from PCL.discord_client import DiscordRequester
import asyncio


async def get_channel_list(token: str, server_id: int) -> List[Channel]:
    reqeuster = DiscordRequester(token)
    return [channel async for channel in reqeuster.get_guild_channels(server_id)]


channel_types = {
    0: "guild_text",
    2: "guild_voice",
    4: "guild_category",
    5: "guild_news",
    6: "guild_store",
    10: "guild_news_thread",
    11: "guild_public_thread",
    12: "guild_private_thread",
    13: "guild_stage_voice",
}


token = input("Enter your token: ")
server_id = int(input("Enter server id: "))

channel_list = asyncio.run(get_channel_list(token, server_id))
for channel in channel_list:
    print(f"{channel.name}: {channel_types[channel.type]} | {channel.id}")
