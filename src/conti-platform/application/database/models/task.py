from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import SlugKey, UUIDAuditBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
if TYPE_CHECKING:
    from .user_role import UserRole
    from .user import User

class Task(UUIDAuditBase):
    """A task that can be assigned to a user or agent."""
    
    __tablename__ = "task"
    __pii_columns__ = {"name", "description"}
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(nullable=True, default=None)
    task_status: Mapped[str] = mapped_column(nullable=False, index=True)
    assignee_id: Mapped[str] = mapped_column(nullable=True, index=True)
    
    
    