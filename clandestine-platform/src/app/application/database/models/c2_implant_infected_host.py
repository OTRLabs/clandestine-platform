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


class CommandNControlImplantInfectedHost(UUIDAuditBase):
    '''A host with an active implant running on it. The host was a target, that was in scope of the project/operation & was infected via a method that you can optionally provide'''
    __tablename__: str = "c2_implant_infected_host"
    __table_args__: dict = (
        Index('ix_c2_implant_infected_host_name', 'c2_implant_infected_host_name'),
        {"comment": "Command and control implant infected host data used to track events and meetings"}
    )
    
    c2_implant_infected_host_name: Mapped[str] = mapped_column(String, nullable=False, comment="Name of the infected host")
    c2_implant_infected_host_description: Mapped[str] = mapped_column(String, nullable=True, comment="Description of the infected host")
    c2_implant_infected_host_public_hostname: Mapped[str] = mapped_column(String, nullable=False, comment="Public hostname or IP of the infected host")
    c2_implant_infected_host_infected_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Date the host was infected")
    c2_implant_infected_host_infected_method: Mapped[str] = mapped_column(String, nullable=True, comment="Method used to infect the host")
    c2_implant_infected_host_infected_by: Mapped[str] = mapped_column(String, nullable=False, comment="Name of the implant that infected the host")
    c2_implant_infected_host_infected_by_description: Mapped[str] = mapped_column(String, nullable=True, comment="Description of the implant that infected the host")
    c2_implant_infected_host_infected_by_callback_url: Mapped[str] = mapped_column(String, nullable=False, comment="URL for the implant to callback to")
    c2_implant_infected_host_lifetime: Mapped[Lifetime] = relationship("Lifetime", back_populates="c2_implant_infected_host", uselist=False, lazy="joined")
    c2_implant_infected_host_tasks: Mapped[List[CommandNControlImplantTask]] = relationship("CommandNControlImplantTask", back_populates="c2_implant_infected_host", cascade="all, delete-orphan")
    