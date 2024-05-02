from dataclasses import dataclass
from datetime import datetime


@dataclass
class MemberEntity:
    phone: str
    created_at: datetime
