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


class CommandNControlImplantShell(UUIDAuditBase):
    '''A shell session for an implant running on an infected host communicating with a listener.'''
    __tablename__: str = "c2_implant_shell"
    __table_args__: dict = (
        Index('ix_c2_implant_shell_name', 'c2_implant_shell_name'),
        {"comment": "Command and control implant shell data used to track events and meetings"}
    )
    
    c2_implant_shell_name: Mapped[str] = mapped_column(String, nullable=False, comment="Name of the implant shell")
    c2_implant_shell_description: Mapped[str] = mapped_column(String, nullable=True, comment="Description of the implant shell")
    c2_implant_infected_host: Mapped[str] = mapped_column(String, nullable=False, comment="Infected host of the implant shell")