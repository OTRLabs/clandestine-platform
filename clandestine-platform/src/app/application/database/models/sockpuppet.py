from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional, Dict
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .team import Team
    from .user import User
    from .sockpuppet_alias import SockPuppetAlias
    

class SockPuppet(UUIDAuditBase):
    __tablename__ = "sockpuppet"
    __table_args__ = {"comment": "Sockpuppets are used to obfuscate real identities when engaging with contacts outside of the organization or with 3rd party services"}
    sockpuppet_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Sockpuppet name")
    sockpuppet_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Sockpuppet description")
    sockpuppet_alias: Mapped[SockPuppetAlias] = mapped_column(String(255), nullable=False, comment="Sockpuppet alias")
    sockpuppet_purpose: Mapped[str] = mapped_column(String(2500), nullable=False, comment="Sockpuppet purpose")
    sockpuppet_status: Mapped[str] = mapped_column(String(255), nullable=False, comment="Sockpuppet status") ## Add an enum for this later
    team_operating_sockpuppet: Mapped[Team] = mapped_column(String(255), nullable=False, comment="Team operating the sockpuppet")
    creator_of_sockpuppet: Mapped[User] = mapped_column(String(255), nullable=False, comment="Creator of the sockpuppet")