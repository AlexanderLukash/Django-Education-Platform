import random
from abc import (
    ABC,
    abstractmethod,
)

from django.core.cache import cache

from core.apps.members.entities.members import MemberEntity
from core.apps.members.exceptions.codes import (
    CodeNotFoundException,
    CodesNotEqualException,
)


class BaseCodeService(ABC):
    @abstractmethod
    def generate_code(self, member: MemberEntity) -> str:
        ...

    @abstractmethod
    def validate_code(self, code: str, member: MemberEntity) -> None:
        ...


class DjangoCacheCodeService(BaseCodeService):
    def generate_code(self, member: MemberEntity) -> str:
        code = str(random.randint(100000, 999999)) # noqa
        cache.set(member.phone, code)
        return code

    def validate_code(self, code: str, member: MemberEntity) -> None:
        cached_code = cache.get(member.phone)

        if cached_code is None:
            raise CodeNotFoundException(code=code)

        if cached_code != code:
            raise CodesNotEqualException(
                code=code,
                cached_code=cached_code,
                member=member,
            )
