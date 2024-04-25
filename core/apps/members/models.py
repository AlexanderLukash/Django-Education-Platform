from uuid import uuid4

from django.db import models

from core.apps.common.models import TimedBaseModel


class Member(TimedBaseModel):
    phone = models.CharField(
        verbose_name='Phone Number',
        max_length=20,
        unique=True,
    )
    token = models.CharField(
        verbose_name='User Token',
        max_length=255,
        unique=True,
        default=uuid4,
    )

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = 'Members'
