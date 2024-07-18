from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship


class AgentGroup(UUIDAuditBase):
    '''Groups of AI agents within the application'''
    __tablename__ = "agent_group"
    __table_args__ = {"comment": "Groups of AI agents within the application"}
    
    name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Agent group name")
    description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Agent group description")
    status: Mapped[str] = mapped_column(String(255), nullable=False, comment="Agent group status")
    