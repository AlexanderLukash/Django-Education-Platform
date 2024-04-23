from datetime import datetime

from pydantic import BaseModel

from core.apps.courses.entities.courses import Course as CourseEntity


class CourseSchema(BaseModel):
    id: int  # noqa
    title: str
    description: str
    created_at: datetime
    updated_at: datetime | None = None

    @staticmethod
    def from_entity(entity: CourseEntity) -> 'CourseSchema':
        return CourseSchema(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


CourseListSchema = list[CourseSchema]
