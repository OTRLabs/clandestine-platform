from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .team import Team
    from .user import User
    from .task import Task    

class Scope(UUIDAuditBase):
    __tablename__ = "scope"
    __table_args__ = {"comment": "Scope for the application"}
    
    scope_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Scope name")
    scope_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Scope description")
    scope_status: Mapped[str] = mapped_column(String(255), nullable=False, comment="Scope status")
    scope_start_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Scope start date")
    scope_end_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Scope end date")
    
    scope_creator: Mapped[User] = relationship("User", back_populates="scope", uselist=False, lazy="joined")
    team_assigned: Mapped[Team] = relationship("Team", back_populates="scope", uselist=False, lazy="joined")
    
    tasks: Mapped[list[Task]] = relationship("Task", back_populates="scope", uselist=True, lazy="joined")
    
    def __repr__(self):
        return f"<Scope {self.scope_name}>"
    
