from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .organization import Organization
    from .team import Team
    from .user import User
    from .task import Task
    from .scope import Scope
    from .project import Project
    
class Operation(UUIDAuditBase):
    '''Operations being carried out by teams of users using the platform'''
    __tablename__ = "operation"
    __table_args__ = {"comment": "Operations being carried out by teams of users using the platform"}
    
    operation_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Operation name")
    operation_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Operation description")
    operation_status: Mapped[str] = mapped_column(String(255), nullable=False, comment="Operation status")
    operation_start_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Operation start date")
    operation_end_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Operation end date")
    operation_scope: Mapped[Scope] = relationship("Scope", back_populates="operation", uselist=False, lazy="joined")
    operation_creator: Mapped[User] = relationship("User", back_populates="operation", uselist=False, lazy="joined")
    operation_teams: Mapped[List[Team]] = relationship("Team", back_populates="operation", uselist=True, lazy="joined")
    operation_organization: Mapped[Organization] = relationship("Organization", back_populates="operation", uselist=False, lazy="joined")
    operation_milestones: Mapped[List[Task]] = relationship("Task", back_populates="operation", uselist=True, lazy="joined")
    operation_projects: Mapped[List[Project]] = relationship("Project", back_populates="operation", uselist=True, lazy="joined")
    