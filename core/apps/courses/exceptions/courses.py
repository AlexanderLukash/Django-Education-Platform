from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class CourseNotFoundException(ServiceException):
    course_id: int

    @property
    def message(self) -> str:
        return 'Course not found.'
