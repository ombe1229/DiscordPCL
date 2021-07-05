from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class Response:
    status: int
    body: Any


@dataclass
class User:
    id: str
    username: str
    discriminator: str
    avatar: str
    bot: Optional[bool]
    email: Optional[str]


@dataclass
class Role:
    id: str
    name: str
    color: int
    permissions: str
    managed: bool


@dataclass
class GuildMember:
    nick: Optional[str]
    roles: List[Role]


@dataclass
class Channel:
    """
    `Channel Types`
     - GUILD_TEXT: 0
     - DM: 1
     - GUILD_VOICE: 2
     - GROUP_DM: 3
     - GUILD_CATEGORY: 4
     - GUILD_NEWS: 5
     - GUILD_STORE: 6
     - GUILD_NEWS_THREAD: 10
     - GUILD_PUBLIC_THREAD: 11
     - GUILD_PRIVATE_THREAED: 12
     - GUILD_STAGE_VOICE: 13
    """

    id: str
    type: int
    name: str
    nsfw: bool


@dataclass
class Emoji:
    name: str
    roles: List[Role]
    id: str
    animated: bool
    available: bool


@dataclass
class Guild:
    id: str
    name: str
    icon: str
    owner: bool
    permissions: int


@dataclass
class GuildInfo:
    id: int
    name: str
    icon: str
    description: str
    emojis: List[Emoji]
    banner: str
    owner_id: int
    region: str
    roles: List[Role]
    approximate_member_count: Optional[int]
