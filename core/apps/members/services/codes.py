from abc import (
    ABC,
    abstractmethod,
)

from core.apps.members.entities.members import MemberEntity


class BaseCodeService(ABC):
    @abstractmethod
    def generate_code(self, member: MemberEntity) -> str:
        ...

    @abstractmethod
    def validate_code(self, code: str, member: MemberEntity) -> None:
        ...
