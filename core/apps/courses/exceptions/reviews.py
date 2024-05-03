from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class InvalidReviewRating(ServiceException):
    rating: int

    @property
    def message(self) -> str:
        return 'Rating is not valid.'
