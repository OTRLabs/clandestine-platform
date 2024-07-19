from __future__ import annotations
from datetime import datetime, date
from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, Date, Integer, Index
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
    __table_args__ = (
        Index('ix_calendar_name', 'calendar_name'),
        {"comment": "Calendar data used to track events and meetings"}
    )
    
    calendar_name: Mapped[str] = mapped_column(String, nullable=False, comment="Name of the calendar")
    calendar_description: Mapped[str] = mapped_column(String, nullable=False, comment="Description of the calendar")    
    calendar_start_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Start date of the calendar")
    calendar_end_date: Mapped[date] = mapped_column(Date, nullable=False, comment="End date of the calendar")
    
    events: Mapped[List[Event]] = relationship("Event", back_populates="calendar", cascade="all, delete-orphan")
    months: Mapped[List[CalendarMonth]] = relationship("CalendarMonth", back_populates="calendar", cascade="all, delete-orphan")
    years: Mapped[List[CalendarYear]] = relationship("CalendarYear", back_populates="calendar", cascade="all, delete-orphan")
    weeks: Mapped[List[CalendarWeek]] = relationship("CalendarWeek", back_populates="calendar", cascade="all, delete-orphan")
    days: Mapped[List[CalendarDay]] = relationship("CalendarDay", back_populates="calendar", cascade="all, delete-orphan")
    tasks: Mapped[List[Task]] = relationship("Task", back_populates="calendar", cascade="all, delete-orphan")
