import factory
from factory.django import DjangoModelFactory

from core.apps.courses.models import Course


class CourseModelFactory(DjangoModelFactory):
    title = factory.Faker('first_name')
    description = factory.Faker('text')

    class Meta:
        model = Course
