from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Credential(UUIDAuditBase):
    __name__ = "credential"
    __table_args__ = {"comment": "Credentials found & collected during operations"}
    credential_label: Mapped[str] = mapped_column(String(255), nullable=False, comment="Credential label")
    credential_value: Mapped[str] = mapped_column(String(255), nullable=False, comment="Credential value")
    credential_service: Mapped[str] = mapped_column(String(255), nullable=False, comment="Credential service")
    
    