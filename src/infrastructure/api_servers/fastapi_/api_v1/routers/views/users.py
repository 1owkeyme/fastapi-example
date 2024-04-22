import typing as t

from common import StrictBaseModel
from domain import entities


class UserId(StrictBaseModel):
    id: int

    @classmethod
    def from_user_id_entity(cls, user_id_entity: entities.user.UserId) -> t.Self:
        return cls(id=user_id_entity.id)

    def to_entity(self) -> entities.user.UserId:
        return entities.user.UserId(id=self.id)


class UserPublic(UserId):
    username: str

    @classmethod
    def from_entity(cls, entity: entities.user.UserPublic) -> t.Self:
        return cls(id=entity.id, username=entity.username)
