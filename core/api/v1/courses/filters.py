from ninja import Schema


class CourseFilters(Schema):
    search: str | None = None
