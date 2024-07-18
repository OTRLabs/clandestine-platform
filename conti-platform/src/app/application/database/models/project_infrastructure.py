from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .project_infrastructure_host import ProjectInfrastructureHost    
class ProjectInfrastructure(UUIDAuditBase):
    __tablename__ = "project_infrastructure"
    __table_args__ = {"comment": "Infrastructure used for a project"}
    
    hosts_used_by_project: Mapped[List[ProjectInfrastructureHost]] = relationship("ProjectInfrastructureHost", back_populates="project_infrastructure")
    