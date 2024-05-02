from dataclasses import (
    dataclass,
    field,
)

from core.apps.common.enums import EntityStatus
from core.apps.courses.entities.courses import Course
from core.apps.members.entities.members import MemberEntity as Member


@dataclass
class CourseReviewEntity:
    rating: int
    member: Member | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    course: Course | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    text: str = field(default='')
