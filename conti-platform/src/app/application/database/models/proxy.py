from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from .team import Team
    from .user import User
    from .task import Task
    from .scope import Scope
    from .project import Project
    
    
class ProxyServer(UUIDAuditBase):
    __tablename__ = "proxy_server"
    __table_args__ = {"comment": "Proxy server information"}
    __pii_columns__ = ["proxy_ip", "proxy_port", "proxy_username", "proxy_password"]
    