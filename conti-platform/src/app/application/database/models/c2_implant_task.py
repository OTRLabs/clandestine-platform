from __future__ import annotations
from datetime import datetime, date
from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, Date, Integer, Index, func, ForeignKey, Column, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .event import Event
    from .calendar import Calendar
    from .task import Task
    from .c2_listener_protocol import CommandNControlListenerProtocol
    from .lifetime import Lifetime



class CommandNControlImplantTask(UUIDAuditBase):
    __tablename__ = 'c2_implant_task'

    id = Column(Integer, primary_key=True)
    implant_id = Column(Integer, ForeignKey('c2_implant.id'))
    implant = relationship('CommandNControlImplant', back_populates='tasks')
    task_id = Column(Integer, ForeignKey('task.id'))
    task = relationship('Task', back_populates='implants')
    status = Column(String(255))
    output = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<CommandNControlImplantTask(id={self.id}, implant_id={self.implant_id}, task_id={self.task_id}, status={self.status}, output={self.output}, created_at={self.created_at}, updated_at={self.updated_at})>'