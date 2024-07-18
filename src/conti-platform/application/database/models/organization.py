from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .user import User
    from .team import Team

class Organization(UUIDAuditBase):
    """An organization that uses the platform"""
    __tablename__ = "organization"
    __table_args__ = {"comment": "An organization that uses the platform"}
    
    organization_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Organization name")
    organization_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Organization description")
    organization_status: Mapped[str] = mapped_column(String(255), nullable=False, comment="Organization status")
    organization_start_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Organization start date")
    
    organization_creator: Mapped[User] = relationship("User", back_populates="organization", uselist=False, lazy="joined")
    organization_teams: Mapped[List[Team]] = relationship("Team", back_populates="organization", uselist=True, lazy="joined")
    #organization_funds: Mapped[List[Fund]] = relationship("Fund", back_populates="organization", uselist=True, lazy="joined")    
