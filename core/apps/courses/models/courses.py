from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.courses.entities.courses import Course as CourseEntity


class Course(TimedBaseModel):
    title = models.CharField(
        verbose_name='Name of the course',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Course description',
        blank=True,
    )
    is_visible = models.BooleanField(
        verbose_name='Is the course visible in the system',
        default=True,
    )

    def to_entity(self) -> CourseEntity:
        return CourseEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
