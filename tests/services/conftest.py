import pytest

from core.apps.courses.services.courses import ORMCourseService


@pytest.fixture()
def course_service() -> ORMCourseService:
    return ORMCourseService()
