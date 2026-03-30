from typing import TYPE_CHECKING, Annotated
from fastapi import Depends

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, declared_attr, relationship

from backend.core.models import Base, db_helper

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from backend.core.models import User


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[int]):
    pass

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False
        )

    @declared_attr
    def user(cls) -> Mapped["User"]:
        return relationship("User", back_populates="access_tokens")

    @classmethod
    async def get_db(
        cls,
        session: Annotated[
            "AsyncSession",
            Depends(db_helper.session_getter),
        ],
    ):
        yield SQLAlchemyAccessTokenDatabase(session, cls)

    def __str__(self):
        return self.token
