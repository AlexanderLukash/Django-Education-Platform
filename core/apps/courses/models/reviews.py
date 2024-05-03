from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.courses.entities.courses import CourseEntity
from core.apps.courses.entities.reviews import CourseReviewEntity
from core.apps.members.entities.members import MemberEntity


class CourseReviewModel(TimedBaseModel):
    member = models.ForeignKey(
        to='members.Member',
        verbose_name='Reviewer',
        related_name='course_reviews',
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        to='courses.Course',
        verbose_name='Course',
        related_name='course_reviews',
        on_delete=models.CASCADE,
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name='Rating',
        default=1,
    )
    text = models.TextField(
        verbose_name='Review text',
        blank=True,
        default='',
    )
    is_approved = models.BooleanField(
        default=False,
    )

    def __str__(self) -> str:
        return f'{self.course.title, self.member.phone}'

    def to_entity(self) -> CourseReviewEntity:
        return CourseReviewEntity(
            id=self.id,
            rating=self.rating,
            text=self.text,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @classmethod
    def from_entity(
            cls,
            review: CourseReviewEntity,
            course: CourseEntity,
            member: MemberEntity,
    ) -> 'CourseReviewModel':
        return cls(
            pk=review.id,
            course_id=course.id,
            member_id=member.id,
            rating=review.rating,
            text=review.text,
        )

    class Meta:
        verbose_name = 'Course review'
        verbose_name_plural = 'Course reviews'
        unique_together = (
            ('member', 'course'),
        )
