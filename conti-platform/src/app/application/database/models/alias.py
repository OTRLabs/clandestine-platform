from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional, Dict
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .team import Team
    from .user import User
    
class Alias(UUIDAuditBase):
    """Aliases used to obfuscate real identities when engaging with contacts outside of the organization or with 3rd party services"""
    __tablename__ = "alias"
    __table_args__ = {"comment": "Aliases used to obfuscate real identities when engaging with contacts outside of the organization"}
    
    alias_status: List = ["active", "inactive"]
    alias_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Alias name")
    alias_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Alias description")
    alias_status: Mapped[str] = mapped_column(String(255), nullable=False, comment="Alias status") ## Add an enum for this later
    alias_start_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Alias start date")
    alias_end_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Alias end date")
    alias_accounts: Mapped[List[Dict[str, str]]] = relationship("User", back_populates="alias", uselist=True, lazy="joined")
    