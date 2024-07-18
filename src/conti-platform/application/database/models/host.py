from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .host_service import HostService
    
    
class Host(UUIDAuditBase):
    '''Hosts in a projects scope'''
    name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Host name")
    ip: Mapped[str] = mapped_column(String(255), nullable=False, comment="Host IP")
    open_ports: Mapped[list[int]] = mapped_column(String(255), nullable=False, comment="Open ports")
    services: Mapped[list[HostService]] = relationship("ScopeHostService", back_populates="hosts", uselist=True, lazy="joined")
    