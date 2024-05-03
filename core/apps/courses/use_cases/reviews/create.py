from dataclasses import dataclass

from core.apps.courses.entities.reviews import CourseReviewEntity
from core.apps.courses.services.courses import BaseCourseService
from core.apps.courses.services.reviews import (
    BaseCourseReviewService,
    BaseCourseReviewValidator,
)
from core.apps.members.services.members import BaseMemberService


@dataclass
class CreateCourseReviewUseCase:
    review_service: BaseCourseReviewService
    member_service: BaseMemberService
    course_service: BaseCourseService
    validator_service: BaseCourseReviewValidator

    def execute(
            self,
            member_token: str,
            course_id: int,
            review: CourseReviewEntity,
    ) -> CourseReviewEntity:
        member = self.member_service.get_by_token(token=member_token)
        course = self.course_service.get_course_by_id(course_id=course_id)
        self.validator_service.validate(review=review, course=course, member=member)
        saved_review = self.review_service.save_review(member=member, course=course, review=review)

        return saved_review
