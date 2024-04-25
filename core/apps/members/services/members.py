from abc import (
    ABC,
    abstractmethod,
)

from core.apps.members.entities.members import MemberEntity


class BaseMemberService(ABC):
    @abstractmethod
    def get_or_create(self, phone: str) -> MemberEntity:
        ...

    @abstractmethod
    def generate_token(self, member: MemberEntity) -> str:
        ...
