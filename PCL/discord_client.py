from typing import Optional
from PCL.utils.requester import Requester


class DiscordRequester:
    def __init__(self, token: str):
        self.requester = Requester(
            "https://discord.com/api/v9/", {"Authorization": token}
        )

    async def get_user_guilds(self):
        return await self.requester.get("users/@me/guilds")

    async def get_guild(self, guild_id: int, with_counts: Optional[bool] = False):
        return await self.requester.get(
            f"guilds/{guild_id}", params={"with_counts": f"{with_counts}"}
        )

    async def get_guild_channels(self, guild_id: int):
        return await self.requester.get(f"guilds/{guild_id}/channels")
