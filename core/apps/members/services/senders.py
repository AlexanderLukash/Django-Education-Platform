from abc import (
    ABC,
    abstractmethod,
)

from core.apps.members.entities.members import MemberEntity


class BaseSenderService(ABC):
    @abstractmethod
    def send_code(self, code: str, member: MemberEntity) -> None:
        ...


class DummySenderService(BaseSenderService):
    def send_code(self, code: str, member: MemberEntity) -> None:
        print(f'Code to user: {member}, send: {code}.')
