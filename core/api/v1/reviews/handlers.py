from django.http import HttpRequest
from ninja import (
    Header,
    Router,
)
from ninja.errors import HttpError

from core.api.schemas import ApiResponse
from core.api.v1.reviews.schemas import (
    CourseReviewInSchema,
    CourseReviewOutSchema,
)
from core.apps.common.exceptions import ServiceException
from core.apps.courses.use_cases.reviews.create import CreateCourseReviewUseCase
from core.project.containers import get_container


router = Router(
    tags=['Reviews'],
)


@router.post('/{course_id}/review', response=ApiResponse[CourseReviewOutSchema], operation_id='createReview')
def create_courses_review(
    request: HttpRequest,
    course_id: int,
    schema: CourseReviewInSchema,
    token: str = Header(alias='Auth-Token'),
) -> ApiResponse[CourseReviewOutSchema]:
    container = get_container()
    use_case: CreateCourseReviewUseCase = container.resolve(CreateCourseReviewUseCase)

    try:
        result = use_case.execute(member_token=token, course_id=course_id, review=schema.to_entity())
    except ServiceException as exception:
        raise HttpError(
            status_code=400,
            message=exception.message,
        ) from exception
    return ApiResponse(data=CourseReviewOutSchema.from_entity(result))
