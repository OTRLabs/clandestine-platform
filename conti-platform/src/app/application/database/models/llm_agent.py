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
    from .scope import Scope
    from .agent_group import AgentGroup
class Agent(UUIDAuditBase):
    '''AI based agents for the application'''
    __tablename__ = "agent"
    __table_args__ = {"comment": "Agents for the application"}
    
    name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Agent name")
    description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Agent description")
    status: Mapped[str] = mapped_column(String(255), nullable=False, comment="Agent status")
    modelfile: Mapped[str] = mapped_column(String(255), nullable=False, comment="Model file")
    modeltype: Mapped[str] = mapped_column(String(255), nullable=False, comment="Model type")
    modelversion: Mapped[str] = mapped_column(String(255), nullable=False, comment="Model version")
    modelprompt: Mapped[str] = mapped_column(String(255), nullable=False, comment="Model prompt")
    modeltools: Mapped[str] = mapped_column(String(255), nullable=False, comment="Model tools")
    
    agent_creator: Mapped[User] = relationship("User", back_populates="agent", uselist=False, lazy="joined")
    team_assigned: Mapped[Team] = relationship("Team", back_populates="agent", uselist=False, lazy="joined")
    agent_tasks: Mapped[list[Task]] = relationship("Task", back_populates="agent", uselist=True, lazy="joined")
    agent_scope: Mapped[Scope] = relationship("Scope", back_populates="agent", uselist=False, lazy="joined")
    agent_group: Mapped[AgentGroup] = relationship("AgentGroup", back_populates="agent", uselist=False, lazy="joined")