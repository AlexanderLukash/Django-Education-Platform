from django.http import HttpRequest
from ninja import Router, Query

from core.api.filters import PaginationIn, PaginationOut
from core.api.schemas import ApiResponse, ListPaginatedResponse
from core.api.v1.courses.filters import CourseFilters
from core.api.v1.courses.schemas import CourseSchema
from core.apps.courses.services.courses import BaseCourseService, ORMCourseService

router = Router(
    tags=['Courses']
)


@router.get('', response=ApiResponse[ListPaginatedResponse[CourseSchema]])
def get_courses_list_handler(
        request: HttpRequest,
        filters: Query[CourseFilters],
        pagination_in:
        Query[PaginationIn]
) -> ApiResponse[ListPaginatedResponse[CourseSchema]]:
    service: BaseCourseService = ORMCourseService()
    course_list = service.get_course_list(filters=filters, pagination=pagination_in)
    course_count = service.get_course_count(filters=filters)
    items = [CourseSchema.from_entity(obj) for obj in course_list]
    pagination_out = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=course_count
    )

    return ApiResponse(data=ListPaginatedResponse(items=items, pagination=pagination_out))
