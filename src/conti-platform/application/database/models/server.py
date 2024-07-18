from __future__ import annotations
from sqlalchemy import String
from advanced_alchemy.base import UUIDAuditBase
from typing import Dict, TYPE_CHECKING, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship









if TYPE_CHECKING:
    from .server_config import ServerConfig
    from .project_infrastructure_host_types import ProjectInfrastructureHostTypes, ProxyTypes
class Server(UUIDAuditBase):
    server_type: ProjectInfrastructureHostTypes
    config: ServerConfig
    description: Mapped[str, str]
    proxy_type: Optional[ProxyTypes] = None
    additional_info: Optional[Dict[str, str]] = None
