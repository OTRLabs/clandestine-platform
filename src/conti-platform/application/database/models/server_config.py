from __future__ import annotations
from sqlalchemy import String
from advanced_alchemy.base import UUIDAuditBase
from typing import Dict, TYPE_CHECKING, Optional
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship






class ServerConfig(UUIDAuditBase):
    hostname: Mapped[str] = mapped_column(String(255), nullable=False, comment="Server hostname")
    ip_address: Mapped[str] = mapped_column(String(255), nullable=False, comment="Server IP address")
    port: Mapped[int] = mapped_column(Integer, nullable=False, comment="Server port")
    username: Mapped[str] = mapped_column(String(255), nullable=False, comment="Server username")
    password: Mapped[str] = mapped_column(String(255), nullable=False, comment="Server password")