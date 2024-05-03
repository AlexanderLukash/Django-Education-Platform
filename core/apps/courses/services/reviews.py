from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.courses.entities.courses import CourseEntity as CourseEntity
from core.apps.courses.entities.reviews import CourseReviewEntity
from core.apps.courses.exceptions.reviews import InvalidReviewRating
from core.apps.courses.models import CourseReviewModel
from core.apps.members.entities.members import MemberEntity


class BaseCourseReviewService(ABC):
    @abstractmethod
    def save_review(
            self,
            member: MemberEntity,
            course: CourseEntity,
            review: CourseReviewEntity,
    ) -> CourseReviewEntity:
        ...


class ORMCourseReviewService(BaseCourseReviewService):
    def save_review(
            self,
            member: MemberEntity,
            course: CourseEntity,
            review: CourseReviewEntity,
    ) -> CourseReviewEntity:
        review_dto = CourseReviewModel.from_entity(
            review=review,
            course=course,
            member=member,
        )
        review_dto.save()
        return review_dto.to_entity()


class BaseCourseReviewValidator(ABC):

    @abstractmethod
    def validate(
            self,
            review: CourseReviewEntity,
            member: MemberEntity | None = None,
            course: CourseEntity | None = None,
    ):
        ...


class CourseReviewValidatorService(BaseCourseReviewValidator):
    def validate(
            self,
            review: CourseReviewEntity,
            *args,
            **kwargs,
    ):
        if not (1 <= review.rating <= 5):
            raise InvalidReviewRating(rating=review.rating)


@dataclass
class ComposedCourseReviewValidator(BaseCourseReviewValidator):
    validators: list[BaseCourseReviewValidator]

    def validate(
            self,
            review: CourseReviewEntity,
            member: MemberEntity | None = None,
            course: CourseEntity | None = None,
    ):
        for validator in self.validators:
            validator.validate(review=review, member=member, course=course)
