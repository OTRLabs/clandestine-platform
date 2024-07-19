from __future__ import annotations
from datetime import datetime, date
from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, Date, Integer, Index, func, ForeignKey, Column, Text, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from .event import Event
    from .calendar import Calendar
    from .task import Task
    from .c2_listener_protocol import CommandNControlListenerProtocol
    from .lifetime import Lifetime
    from .c2_implant import CommandNControlImplant

class CommandNControlImplantTask(UUIDAuditBase):
    __tablename__ = 'c2_implant_task'
    __table_args__ = (
        Index('ix_c2_implant_task_name', 'c2_implant_task_name'),
        {"comment": "Command and control implant task data used to track events and meetings"}
    )

    c2_implant_task_name: Mapped[str] = mapped_column(String, nullable=False, comment="Name of the implant task")
    c2_implant_task_description: Mapped[str] = mapped_column(String, nullable=False, comment="Description of the implant task")
    c2_implant_task_data: Mapped[dict] = mapped_column(Text, nullable=False, comment="Data of the implant task")
    c2_implant_task_created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False, comment="Timestamp of when the implant task was created")
    c2_implant_task_updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False, comment="Timestamp of when the implant task was last updated")
    c2_implant_task_due_date: Mapped[date] = mapped_column(Date, nullable=True, comment="Due date of the implant task")
    c2_implant_task_priority: Mapped[int] = mapped_column(Integer, nullable=True, comment="Priority of the implant task")
    c2_implant_task_is_assigned_to: Mapped[str] = mapped_column(String, nullable=True, comment="User assigned to the implant task")
    c2_implant_task_completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment="Flag indicating if the implant task is completed")
    c2_implant_task_completed_at: Mapped[datetime] = mapped_column(DateTime, nullable=True, comment="Timestamp of when the implant task was completed")
    c2_implant_emergency_kill_task_time: Mapped[datetime] = mapped_column(DateTime, nullable=True, comment="Timestamp of when to trigger a tasks emergency kill switch. For use when a task has an optimal timeframe & should not be executed outside of it.")
    