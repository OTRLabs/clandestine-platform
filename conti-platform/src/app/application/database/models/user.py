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
    from .team_member import TeamMember
    from .user_pgpkey import UserPGPKey
class User(UUIDAuditBase):
    __tablename__ = "user_account"
    __table_args__ = {"comment": "User accounts for application access"}
    __pii_columns__ = ["email"]
    
    user_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="User name")
    user_display_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="User display name (public name. think like your @ on twitter)")
    user_login_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="User login name, private name for login")
    user_email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, comment="User email address")
    user_xmpp: Mapped[str] = mapped_column(String(255), nullable=True, comment="User XMPP address")
    user_xmpp_encryption: Mapped[str] = mapped_column(String(255), nullable=True, comment="User XMPP encryption") # // create an Enum for this
    # user_prefered_contact: Mapped[str] = mapped_column(String(255), nullable=True, comment="User prefered contact") 
    # ## ^^ // create an Enum for this
    user_pgp_key: Mapped[UserPGPKey] = relationship("UserPGPKey", back_populates="user", uselist=False, lazy="joined")
    user_pgp_fingerprint: Mapped[str] = mapped_column(String(40), nullable=True, comment="PGP key fingerprint")
    user_role: Mapped[UserRole] = relationship("UserRole", back_populates="user", uselist=False, lazy="joined")
    
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False, comment="User password")
    user_phishing_security_phrase: Mapped[str] = mapped_column(String(255), nullable=True, comment="User phishing security phrase")
    roles: Mapped[list[UserRole]] = relationship(
        back_populates="user",
        lazy="selectin",
        uselist=True,
        cascade="all, delete",
    )
    teams: Mapped[list[TeamMember]] = relationship(
        back_populates="user",
        lazy="selectin",
        uselist=True,
        cascade="all, delete",
        viewonly=True,
    )