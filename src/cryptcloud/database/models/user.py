from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    #from .oauth_account import UserOauthAccount
    #from .team_member import TeamMember
    #from .user_role import UserRole
    
    
class User(UUIDAuditBase):
    __tablename__ = "user_account"
    __table_args__ = {"comment": "User accounts for application access"}
    __pii_columns__ = ["email"]
    
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, comment="User email address")
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False, comment="User password")