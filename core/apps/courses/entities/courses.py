from dataclasses import dataclass
from datetime import datetime


@dataclass
class CourseEntity:
    id: int # noqa
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
