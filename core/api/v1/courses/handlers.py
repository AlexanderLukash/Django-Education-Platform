from django.http import HttpRequest
from ninja import Router

from core.api.v1.courses.schemas import CourseListSchemas

router = Router(
    tags=['Courses']
)


@router.get('', response=CourseListSchemas)
async def get_courses_list_handler(request: HttpRequest) -> CourseListSchemas:
    return []
