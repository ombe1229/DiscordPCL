from dataclasses import dataclass
from typing import Any


@dataclass
class Response:
    status: int
    body: Any