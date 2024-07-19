from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from .host_service import HostService


class ScopeHostService(UUIDAuditBase):
    '''A service running on a host in the scope of a project'''
    in_scope_host_service: Mapped[HostService] = relationship("ScopeHosts", back_populates="services", uselist=False, lazy="joined")