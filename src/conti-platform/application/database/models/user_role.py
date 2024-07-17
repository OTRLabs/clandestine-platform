from __future__ import annotations

from datetime import datetime, date, UTC

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy
if TYPE_CHECKING:
    from .user import User    

class UserRole(UUIDAuditBase):
    
    """User Role."""

    __tablename__ = "user_account_role"
    __table_args__ = {"comment": "Links a user to a specific role."}
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user_account.id", ondelete="cascade"), nullable=False)
    role_id: Mapped[UUID] = mapped_column(ForeignKey("role.id", ondelete="cascade"), nullable=False)
    assigned_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))

    # -----------
    # ORM Relationships
    # ------------
    user: Mapped[User] = relationship(back_populates="roles", innerjoin=True, uselist=False, lazy="joined")
    user_name: AssociationProxy[str] = association_proxy("user", "name")
    user_email: AssociationProxy[str] = association_proxy("user", "email")
    role: Mapped[Role] = relationship(back_populates="users", innerjoin=True, uselist=False, lazy="joined")
    role_name: AssociationProxy[str] = association_proxy("role", "name")
    role_slug: AssociationProxy[str] = association_proxy("role", "slug")