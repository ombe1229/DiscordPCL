from PCL.utils.objects import Channel, Guild, GuildInfo
from typing import Iterator, Optional
from PCL.utils.requester import Requester


class DiscordRequester:
    def __init__(self, token: str):
        self.requester = Requester(
            "https://discord.com/api/v9/", {"Authorization": token}
        )

    async def get_user_guilds(self) -> Iterator[Guild]:
        response = await self.requester.get("users/@me/guilds")
        for guild in response.body:
            yield Guild(
                guild["id"],
                guild["name"],
                guild["icon"],
                guild["owner"],
                guild["permissions"],
            )

    async def get_guild(
        self, guild_id: int, with_counts: Optional[bool] = False
    ) -> GuildInfo:
        response = await self.requester.get(
            f"guilds/{guild_id}", params={"with_counts": f"{with_counts}"}
        )
        guild = response.body
        return GuildInfo(
            guild["id"],
            guild["name"],
            guild["icon"],
            guild["description"],
            guild["emojis"],
            guild["banner"],
            guild["owner_id"],
            guild["region"],
            guild["roles"],
            guild.get("approximate_member_count"),
        )

    async def get_guild_channels(self, guild_id: int):
        return await self.requester.get(f"guilds/{guild_id}/channels")
