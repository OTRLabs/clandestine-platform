from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship



class Project(UUIDAuditBase):
    __tablename__ = "project"
    __table_args__ = {"comment": "Projects for the application"}
    
    project_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Project name")
    project_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Project description")
    project_status: Mapped[str] = mapped_column(String(255), nullable=False, comment="Project status")
    project_start_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Project start date")
    
    