from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class UserPGPKey(UUIDAuditBase):
    __tablename__ = "user_pgpkey"
    __table_args__ = {"comment": "User PGP keys for encryption, identity verification, and signing"}
    __pii_columns__ = ["key"]
    
    user_id: Mapped[str] = mapped_column(String(36), nullable=False, comment="User ID")
    key: Mapped[str] = mapped_column(String(4096), nullable=False, comment="PGP key")
    fingerprint: Mapped[str] = mapped_column(String(40), nullable=False, comment="PGP key fingerprint")
    