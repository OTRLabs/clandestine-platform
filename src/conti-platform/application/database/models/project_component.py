from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
if TYPE_CHECKING:
    from .team import Team
    from .task import Task

class ProjectComponent(UUIDAuditBase):
    __tablename__ = "project_component"
    __table_args__ = {"comment": "Project Component for the application"}
    
    component_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Component name")
    component_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Component description")
    component_status: Mapped[str] = mapped_column(String(255), nullable=False, comment="Component status")
    component_start_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Component start date")
    component_end_date: Mapped[date] = mapped_column(Date, nullable=True, comment="Component end date")
    
    tasks: Mapped[list[Task]] = relationship("Task", back_populates="project_component", uselist=True, lazy="joined")
    team_assigned: Mapped[Team] = relationship("Team", back_populates="project_component", uselist=False, lazy="joined")
    