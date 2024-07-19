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

class CalendarDay(UUIDAuditBase):
    __tablename__ = "calendar_day"
    __table_args__ = (
        Index('ix_calendar_day_date', 'calendar_day_date'),
        {"comment": "Calendar day data used to track events and meetings"}
    )
    
    calendar_day: Mapped[int] = mapped_column(Integer, nullable=False, comment="Calendar day")
    calendar_day_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Date of the calendar day")
    
    events: Mapped[List[Event]] = relationship("Event", back_populates="calendar_day", cascade="all, delete-orphan")
    tasks: Mapped[List[Task]] = relationship("Task", back_populates="calendar_day", cascade="all, delete-orphan")
    
    calendar_id: Mapped[Optional[int]] = mapped_column(ForeignKey('calendar.id'), nullable=False)
    calendar: Mapped[Calendar] = relationship("Calendar", back_populates="days")
