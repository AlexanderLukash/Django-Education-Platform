from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from django.db.models import Q

from core.api.filters import PaginationIn
from core.apps.courses.entities.courses import CourseEntity
from core.apps.courses.exceptions.courses import CourseNotFoundException
from core.apps.courses.filters.courses import CourseFilters
from core.apps.courses.models.courses import Course as CourseModel


class BaseCourseService(ABC):
    @abstractmethod
    def get_course_list(
            self,
            filters: CourseFilters,
            pagination: PaginationIn,
    ) -> Iterable[CourseEntity]:
        ...

    @abstractmethod
    def get_course_count(self, filters: CourseFilters) -> int:
        ...

    @abstractmethod
    def get_course_by_id(self, course_id: int) -> CourseEntity:
        ...


class ORMCourseService(BaseCourseService):
    @staticmethod
    def _build_course_query(filters: CourseFilters) -> Q:
        query = Q(is_visible=True)

        if filters.search is not None:
            query &= Q(title__icontains=filters.search) | Q(
                description__icontains=filters.search,
            )
        return query

    def get_course_list(
            self,
            filters: CourseFilters,
            pagination: PaginationIn,
    ) -> Iterable[CourseEntity]:
        query = self._build_course_query(filters)
        qs = CourseModel.objects.filter(query)[
             pagination.offset: pagination.offset + pagination.limit
        ]

        return [course.to_entity() for course in qs]

    def get_course_count(self, filters: CourseFilters) -> int:
        query = self._build_course_query(filters)
        return CourseModel.objects.filter(query).count()

    def get_course_by_id(self, course_id: int) -> CourseEntity:
        try:
            course_dto = CourseModel.objects.get(id=course_id)
        except CourseModel.DoesNotExist:
            raise CourseNotFoundException(course_id=course_id)
        return course_dto.to_entity()
