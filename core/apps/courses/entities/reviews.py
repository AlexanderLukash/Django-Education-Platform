from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime

from core.apps.common.enums import EntityStatus
from core.apps.courses.entities.courses import CourseEntity
from core.apps.members.entities.members import MemberEntity as Member


@dataclass
class CourseReviewEntity:
    id: int | None = field(default=None, kw_only=True)  # noqa
    rating: int
    member: Member | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    course: CourseEntity | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    text: str = field(default='')
    created_at: datetime | None = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = field(default=None)
