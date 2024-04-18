from django.db import models

from core.apps.common.models import TimedBaseModel


class Course(TimedBaseModel):
    title = models.CharField(
        verbose_name='Name of the course',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Course description',
        blank=True
    )
    is_visible = models.BooleanField(
        verbose_name='Is the course visible in the system',
        default=True
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
