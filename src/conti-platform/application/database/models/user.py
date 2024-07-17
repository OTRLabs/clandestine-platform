from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    #from .oauth_account import UserOauthAccount
    #from .team_member import TeamMember
    from .user_role import UserRole
    
    
class User(UUIDAuditBase):
    __tablename__ = "user_account"
    __table_args__ = {"comment": "User accounts for application access"}
    __pii_columns__ = ["email"]
    
    name: Mapped[str] = mapped_column(String(255), nullable=False, comment="User name")
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, comment="User email address")
    xmpp: Mapped[str] = mapped_column(String(255), nullable=True, comment="User XMPP address")
    user_role: Mapped[UserRole] = relationship("UserRole", back_populates="user", uselist=False, lazy="joined")
    
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False, comment="User password")
    
    