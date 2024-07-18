from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship



class DocumentType(UUIDAuditBase):
    __name__ = "document_type"
    __table_args__ = {"comment": "Document types for the application"}
    
    name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Document type name")
    description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Document type description")
    status: Mapped[str] = mapped_column(String(255), nullable=False, comment="Document type status")
    