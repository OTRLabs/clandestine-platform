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
    from .c2_listener_protocol import CommandNControlListenerProtocol
    from .lifetime import Lifetime
    from .agent import Agent

class CommandNControlListener(UUIDAuditBase):
    __tablename__ = "c2_listener"
    __table_args__ = (
        Index('ix_c2_listener_name', 'c2_listener_name'),
        {"comment": "Command and control listener data used to track events and meetings"}
    )
    
    c2_listener_name: Mapped[str] = mapped_column(String, nullable=False, comment="Name of the listener")
    c2_listener_description: Mapped[str] = mapped_column(String, nullable=False, comment="Description of the listener")

    c2_public_hostname: Mapped[str] = mapped_column(String, nullable=False, comment="Public hostname or IP of the listener")
    c2_listener_listening_address: Mapped[str] = mapped_column(String, nullable=False, comment="Listen address of the listener")
    c2_listener_listening_port: Mapped[int] = mapped_column(Integer, nullable=False, comment="Listening port of the listener")
    c2_listener_protocol: Mapped[CommandNControlListenerProtocol] = relationship("CommandNControlProtocol", back_populates="listeners")
    
    c2_lifetime: Mapped[Lifetime] = relationship("Lifetime", back_populates="c2_listener", uselist=False, lazy="joined")
    c2_listener_agent: Mapped[Agent] = relationship("Agent", back_populates="c2_listener", uselist=False, lazy="joined")