from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from .team import Team
    from .user import User
    from .task import Task
    from .scope import Scope
    from .project import Project
    from .c2_status import CommandNControlStatus
    
    
class CommandNControl(UUIDAuditBase):
    __tablename__ = "command_n_control"
    __table_args__ = {"comment": "Command and control server information"}
    __pii_columns__ = ["server_ip", "server_port"]
    
    c2_server_ip: Mapped[str] = mapped_column(String(255), nullable=False, comment="Command and control server IP address")
    c2_server_port: Mapped[int] = mapped_column(Integer, nullable=False, comment="Command and control server port number")
    c2_server_status: Mapped[str] = mapped_column(String(255), nullable=False, comment="Command and control server status")
    
    c2_status: Mapped[CommandNControlStatus] = relationship("CommandNControlStatus", back_populates="c2", uselist=False, lazy="joined")
    c2_start_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Command and control server start date")
    
    c2_creator: Mapped[User] = relationship("User", back_populates="c2", uselist=False, lazy="joined")
    team_responsible_for_c2: Mapped[Team] = relationship("Team", back_populates="c2", uselist=False, lazy="joined")