from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class MemberTokenInvalidException(ServiceException):
    token: str

    @property
    def message(self) -> str:
        return 'A member with provided token is not found.'
