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
    from .llm_agent_group import AgentGroup
class LargeLanguageModelAgent(UUIDAuditBase):
    '''An LLM based agent that exists within the application'''
    __tablename__ = "agent"
    __table_args__ = {"comment": "Agents for the application"}
    
    llm_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Agent name")
    llm_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Agent description")
    llm_status: Mapped[str] = mapped_column(String(255), nullable=False, comment="Agent status")
    llm_modelfile: Mapped[str] = mapped_column(String(255), nullable=False, comment="Model file")
    llm_modeltype: Mapped[str] = mapped_column(String(255), nullable=False, comment="Model type")
    llm_modelversion: Mapped[str] = mapped_column(String(255), nullable=False, comment="Model version")
    llm_modelprompt: Mapped[str] = mapped_column(String(255), nullable=False, comment="Model prompt")
    llm_modeltools: Mapped[str] = mapped_column(String(255), nullable=False, comment="Model tools")
    llm_agent_creator: Mapped[User] = relationship("User", back_populates="agent", uselist=False, lazy="joined")
    llm_team_assigned: Mapped[Team] = relationship("Team", back_populates="agent", uselist=False, lazy="joined")
    llm_agent_tasks: Mapped[list[Task]] = relationship("Task", back_populates="agent", uselist=True, lazy="joined")
    llm_agent_scope: Mapped[Scope] = relationship("Scope", back_populates="agent", uselist=False, lazy="joined")
    llm_agent_group: Mapped[AgentGroup] = relationship("AgentGroup", back_populates="agent", uselist=False, lazy="joined")