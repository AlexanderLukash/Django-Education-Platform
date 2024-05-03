from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime


@dataclass
class MemberEntity:
    id: int | None = field(default=None, kw_only=True)  # noqa
    phone: str
    created_at: datetime
