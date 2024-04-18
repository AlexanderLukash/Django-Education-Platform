from datetime import datetime

from pydantic import BaseModel


class CourseSchemas(BaseModel):
    title: str
    description: str
    created_at: datetime
    updated_at: datetime | None = None


CourseListSchemas = list[CourseSchemas]
