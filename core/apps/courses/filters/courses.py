from dataclasses import dataclass


@dataclass(frozen=True)
class CourseFilters:
    search: str | None = None
