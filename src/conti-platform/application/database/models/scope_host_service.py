from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship



class ScopeHostService(UUIDAuditBase):
    '''A service running on a host in the scope of a project'''
    name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Service Name")
    running_on_port: Mapped[int] = mapped_column(Integer, nullable=False, comment="Port the service is running on")
    service_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Service description")