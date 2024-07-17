from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
if TYPE_CHECKING:
    from .user import User
    from .agent import Agent


class Task(UUIDAuditBase):
    """A task that can be assigned to a user or agent."""
    
    __tablename__ = "task"
    __pii_columns__ = {"name", "description"}
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(nullable=True, default=None)
    task_status: Mapped[str] = mapped_column(nullable=False, index=True)
    task_creator: Mapped[User] = relationship("User", back_populates="created_tasks", uselist=False, lazy="joined")
    task_assignee: Mapped[User] = relationship("User", back_populates="assigned_tasks", uselist=False, lazy="joined")
    task_agent: Mapped[Agent] = relationship("Agent", back_populates="agent_tasks", uselist=False, lazy="joined")
    
    