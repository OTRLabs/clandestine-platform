from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .host import Host
    from .scope_host_service import ScopeHostService
    
    
class ScopeHosts(Host):
    '''Hosts in a projects scope'''

    __tablename__ = "scope_hosts"
    __table_args__ = {"comment": "Hosts in a projects scope"}
    
    hosts_in_scope: Mapped[list[Host]] = relationship("ProjectInfrastructure", back_populates="hosts", uselist=False, lazy="joined")
    hosts_out_of_scope: Mapped[list[Host]] = relationship("ProjectInfrastructure", back_populates="hosts", uselist=False, lazy="joined")