from abc import (
    ABC,
    abstractmethod,
)
from uuid import uuid4

from core.apps.members.entities.members import MemberEntity
from core.apps.members.exceptions.members import MemberTokenInvalidException
from core.apps.members.models import Member as MemberModel


class BaseMemberService(ABC):
    @abstractmethod
    def get_or_create(self, phone: str) -> MemberEntity:
        ...

    @abstractmethod
    def generate_token(self, member: MemberEntity) -> str:
        ...

    @abstractmethod
    def get(self, phone: str) -> MemberEntity:
        ...

    @abstractmethod
    def get_by_token(self, token: str) -> MemberEntity:
        ...


class ORMMemberService(BaseMemberService):
    def get_or_create(self, phone: str) -> MemberEntity:
        user_dto, _ = MemberModel.objects.get_or_create(phone=phone)
        return user_dto.to_entity()

    def get(self, phone: str) -> MemberEntity:
        user_dto = MemberModel.objects.get(phone=phone)
        return user_dto.to_entity()

    def generate_token(self, member: MemberEntity) -> str:
        new_token = str(uuid4())
        MemberModel.objects.filter(phone=member.phone).update(
            token=new_token,
        )
        return new_token

    def get_by_token(self, token: str) -> MemberEntity:
        try:
            user_dto = MemberModel.objects.get(token=token)
        except MemberModel.DoesNotExist:
            raise MemberTokenInvalidException(token=token)
        return user_dto.to_entity()
