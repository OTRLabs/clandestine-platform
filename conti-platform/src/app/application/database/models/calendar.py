from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase
from datetime import datetime
from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .team import Team
    from .user import User
    from .task import Task
    from .scope import Scope
    from .project import Project
    from .event import Event
    from .calendar_month import CalendarMonth
    from .calendar_year import CalendarYear
    from .calendar_week import CalendarWeek
    from .calendar_day import CalendarDay
    
    
class Calendar(UUIDAuditBase):
    __tablename__ = "calendar"
    __table_args__ = {"comment": "Calendar data used to track events and meetings"}
    
    calendar_name: Mapped[str] = mapped_column(String, nullable=False, comment="Name of the calendar")
    calendar_description: Mapped[str] = mapped_column(String, nullable=False, comment="Description of the calendar")    
    calendar_start_date: Mapped[datetime] = mapped_column(Date, nullable=False, comment="Start date of the calendar")
    calendar_end_date: Mapped[datetime] = mapped_column(Date, nullable=False, comment="End date of the calendar")
    
    calendar_event: Mapped[Event] = relationship("Event", back_populates="calendar")
    calendar_month: Mapped[CalendarMonth] = relationship("CalendarMonth", back_populates="calendar")
    calendar_year: Mapped[CalendarYear] = relationship("CalendarYear", back_populates="calendar")
    calendar_week: Mapped[CalendarWeek] = relationship("CalendarWeek", back_populates="calendar")
    calendar_day: Mapped[CalendarDay] = relationship("CalendarDay", back_populates="calendar")
    calendar_tasks: Mapped[Task] = relationship("Task", back_populates="calendar")
    