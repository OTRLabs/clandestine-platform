from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
if TYPE_CHECKING:
    from .user import User
    

class Document(UUIDAuditBase):
    __tablename__ = "document"
    __table_args__ = {"comment": "Document containing relevant information for the application"}
    
    document_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Document name")
    document_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Document description")
    document_url: Mapped[str] = mapped_column(String(255), nullable=False, comment="Document URL in the S3 bucket")
    document_owner: Mapped[User] = relationship("User", back_populates="document", uselist=False, lazy="joined")
    document_add_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Document add date")
    document_update_date: Mapped[date] = mapped_column(Date, nullable=True, comment="Document update date")
    document_tags: Mapped[list[str]] = mapped_column(String(255), nullable=True, comment="Document tags")