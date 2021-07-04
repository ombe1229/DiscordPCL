from PCL.utils.requester import Requester


class DiscordRequester:
    def __init__(self, token: str):
        self.requester = Requester(
            "https://discord.com/api/v9/", {"Authorization": token}
        )

    async def get_user_guilds(self):
        return await self.requester.get("users/@me/guilds")
