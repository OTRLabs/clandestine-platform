from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import SlugKey, UUIDAuditBase
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .user_role import UserRole


class Team(UUIDAuditBase):
    """Team."""

    __tablename__ = "team"

    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None]
    
    
    # -----------
    # ORM Relationships
    # ------------
    members: Mapped[list[TeamMember]] = relationship(
        back_populates="team",
        cascade="all, delete",
        lazy="noload",
        viewonly=True,
    )
    
    roles: Mapped[list[UserRole]] = relationship(
        back_populates="team",
        cascade="all, delete",
        lazy="noload",
        viewonly=True,
    )