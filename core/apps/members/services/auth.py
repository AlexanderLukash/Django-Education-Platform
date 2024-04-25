from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.members.services.codes import BaseCodeService
from core.apps.members.services.members import BaseMemberService
from core.apps.members.services.senders import BaseSenderService


@dataclass(eq=False)
class BaseAuthService(ABC):
    member_service: BaseMemberService
    codes_service: BaseCodeService
    sender_service: BaseSenderService

    @abstractmethod
    def authorize(self, phone: str):
        ...

    @abstractmethod
    def confirm(self, code: str, phone: str):
        ...


class AuthService(BaseAuthService):
    def authorize(self, phone: str):
        member = self.member_service.get_or_create(phone)
        code = self.codes_service.generate_code(member)
        self.sender_service.send_code(code, member)

    def confirm(self, code: str, phone: str):
        member = self.member_service.get(phone)
        self.codes_service.validate_code(code, member)
        return self.member_service.generate_token(member)
