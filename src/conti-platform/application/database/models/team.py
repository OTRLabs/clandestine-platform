from __future__ import annotations

from typing import TYPE_CHECKING
from sqlalchemy import String
from advanced_alchemy.base import SlugKey, UUIDAuditBase
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .user_role import UserRole
    from .team_member import TeamMember

class Team(UUIDAuditBase):
    """A group of users with common permissions.
    Users can create and invite users to a team.
    """

    __tablename__ = "team"
    __pii_columns__ = {"name", "description"}
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(String(length=500), nullable=True, default=None)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    # -----------
    
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