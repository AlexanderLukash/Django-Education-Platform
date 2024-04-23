from dataclasses import dataclass
from datetime import datetime


@dataclass
class Course:
    id: int # noqa
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
