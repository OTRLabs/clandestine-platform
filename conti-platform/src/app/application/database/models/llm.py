from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .llm_agent import LAgent

class LargeLanguageModel(UUIDAuditBase):
    __tablename__ = "llm"
    __table_args__ = {"comment": "Large Language Model data for the application"}
    
    llm_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="LLM name")
    llm_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="LLM description")
    llm_status: Mapped[str] = mapped_column(String(255), nullable=False, comment="LLM status")
    llm_modelfile: Mapped[str] = mapped_column(String(255), nullable=False, comment="LLM Model file")