from __future__ import annotations
from datetime import datetime, date
from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, Date, Integer, Index, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .event import Event
    from .calendar import Calendar
    from .c2_implant_task import CommandNControlImplantTask
    from .c2_listener import CommandNControlListener
    from .c2_listener_protocol import CommandNControlListenerProtocol
    from .lifetime import Lifetime
    
    
    
class CommandNControlImplant(UUIDAuditBase):
    __tablename__ = "c2_implant"
    __table_args__ = (
        Index('ix_c2_implant_name', 'c2_implant_name'),
        {"comment": "Command and control implant data used to track events and meetings"}
    )
    
    c2_implant_name: Mapped[str] = mapped_column(String, nullable=False, comment="Name of the implant")
    c2_implant_description: Mapped[str] = mapped_column(String, nullable=False, comment="Description of the implant")
    
    c2_implant_public_hostname: Mapped[str] = mapped_column(String, nullable=False, comment="Public hostname or IP of the implant")
    c2_implant_listening_address: Mapped[str] = mapped_column(String, nullable=False, comment="Listen address of the implant")
    c2_implant_listening_port: Mapped[int] = mapped_column(Integer, nullable=False, comment="Listening port of the implant")
    c2_implant_protocol: Mapped[CommandNControlListenerProtocol] = relationship("CommandNControlProtocol", back_populates="implants")
    c2_implant_callback_url: Mapped[str] = mapped_column(String, nullable=False, comment="URL for the implant to callback to")
    c2_lifetime: Mapped[Lifetime] = relationship("Lifetime", back_populates="c2_implant", uselist=False, lazy="joined")
    c2_implant_tasks: Mapped[List[CommandNControlImplantTask]] = relationship("CommandNControlImplantTask", back_populates="c2_implant", cascade="all, delete-orphan")
    c2_listener: Mapped[CommandNControlListener] = relationship("CommandNControlListener", back_populates="c2_implant", uselist=False, lazy="joined")
    