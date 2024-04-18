from django.db import models


class TimedBaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Date of creation',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Update date',
        auto_now=True
    )

    class Meta:
        abstract = True
