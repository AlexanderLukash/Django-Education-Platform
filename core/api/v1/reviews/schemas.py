from datetime import datetime

from pydantic import BaseModel

from core.apps.courses.entities.reviews import CourseReviewEntity


class CourseReviewInSchema(BaseModel):
    rating: int = 1
    text: str = ''

    def to_entity(self):
        return CourseReviewEntity(
            rating=self.rating,
            text=self.text,
        )


class CreateCourseReviewSchema(BaseModel):
    course_id: int
    member_token: str
    review: CourseReviewInSchema


class CourseReviewOutSchema(CourseReviewInSchema):
    id: int  # noqa
    created_at: datetime
    updated_at: datetime | None

    @classmethod
    def from_entity(cls, review: CourseReviewEntity) -> 'CourseReviewOutSchema':
        return cls(
            id=review.id,
            rating=review.rating,
            text=review.text,
            created_at=review.created_at,
            updated_at=review.updated_at,
        )
