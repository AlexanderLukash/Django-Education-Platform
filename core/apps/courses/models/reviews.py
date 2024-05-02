from django.db import models

from core.apps.common.models import TimedBaseModel


class CourseReview(TimedBaseModel):
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

    class Meta:
        verbose_name = 'Course review'
        verbose_name_plural = 'Course reviews'
        unique_together = (
            ('member', 'course'),
        )
