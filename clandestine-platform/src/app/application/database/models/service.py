from __future__ import annotations
from datetime import datetime, date
from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, Date, Integer, Index, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .event import Event
    from .calendar import Calendar
    from .task import Task
    from .c2_listener import CommandNControlListener
    from .c2_listener_protocol import CommandNControlListenerProtocol
    from .lifetime import Lifetime
    from .llm_agent import LargeLanguageModelAgent
    
class Service(UUIDAuditBase):
    '''A service that is running on a host exposing itself to a listener address & listener port'''
    service_name: Mapped[str] = mapped_column(String, nullable=False, comment="Name of the service")
    service_description: Mapped[str] = mapped_column(String, nullable=True, comment="Description of the service")
    service_public_hostname: Mapped[str] = mapped_column(String, nullable=False, comment="Public hostname or IP of the service")
    service_listening_address: Mapped[str] = mapped_column(String, nullable=False, comment="Listen address of the service")
    service_listening_port: Mapped[int] = mapped_column(Integer, nullable=False, comment="Listening port of the service")
    service_protocol: Mapped[CommandNControlListenerProtocol] = relationship("CommandNControlProtocol", back_populates="services")
    service_discovered_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Date the service was discovered")
    service_discovered_by_agent: Mapped[LargeLanguageModelAgent] = relationship("LLM_Agent", back_populates="services", uselist=False, lazy="joined")
    