r"""
1. Test products count: product count zero, product count with existing products
2. Test product returns all, w\ paginagion, test filters (description, title, no match)
"""
import pytest
from tests.factories.courses import CourseModelFactory

from core.api.filters import PaginationIn
from core.api.v1.courses.filters import CourseFilters
from core.apps.courses.services.courses import BaseCourseService


@pytest.mark.django_db
def test_get_courses_count_zero(course_service: BaseCourseService):
    """Test courses count zero with no courses in database."""
    courses_count = course_service.get_course_count(CourseFilters())
    assert courses_count == 0, f'{courses_count=}'


@pytest.mark.django_db
def test_get_courses_count_exist(course_service: BaseCourseService):
    """Test courses count exits courses in database."""

    expected_count = 5
    CourseModelFactory.create_batch(size=expected_count)
    courses_count = course_service.get_course_count(CourseFilters())
    assert courses_count == expected_count, f'{courses_count=}'


@pytest.mark.django_db
def test_get_courses_all(course_service: BaseCourseService):
    """Test get all courses in database."""

    expected_count = 5
    courses = CourseModelFactory.create_batch(size=expected_count)
    courses_title = {course.title for course in courses}

    fetched_courses = course_service.get_course_list(CourseFilters(), PaginationIn())
    fetched_titles = {course.title for course in fetched_courses}
    assert len(fetched_titles) == expected_count, f'{fetched_titles=}'
    assert courses_title == fetched_titles, f'{courses_title=}'
