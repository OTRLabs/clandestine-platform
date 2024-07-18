from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .user import User

class Repository(UUIDAuditBase):
    __tablename__ = "repository"
    __table_args__ = {"comment": "Repository containing code relevant to a project in the application"}
    repository_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False, comment="Repository ID")
    repository_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Repository name")
    repository_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Repository description")
    repository_url: Mapped[str] = mapped_column(String(255), nullable=False, comment="Repository URL in the Git instance")
    repository_owner: Mapped[User] = relationship("User", back_populates="repository", uselist=False, lazy="joined")
    repository_add_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Repository add date")
    repository_update_date: Mapped[date] = mapped_column(Date, nullable=True, comment="Repository update date")
    
    
    