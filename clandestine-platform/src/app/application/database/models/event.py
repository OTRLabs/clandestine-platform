from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING, Optional
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .calendar import Calendar
    from .calendar_day import CalendarDay

class Event(UUIDAuditBase):
    __tablename__ = "event"
    __table_args__ = {"comment": "Event data for calendar"}
    #__pii_columns__ = {"name", "event_description"}
    event_name: Mapped[str] = mapped_column(String, nullable=False, comment="Name of the event")
    event_description: Mapped[str] = mapped_column(String, nullable=True, comment="Description of the event")
    event_start: Mapped[datetime] = mapped_column(DateTime, nullable=False, comment="Start time of the event")
    event_end: Mapped[datetime] = mapped_column(DateTime, nullable=False, comment="End time of the event")
    event_location: Mapped[str] = mapped_column(String, nullable=True, comment="Location of the event")
    event_url: Mapped[str] = mapped_column(String, nullable=True, comment="URL of the event")
    calendar_id: Mapped[Optional[int]] = mapped_column(ForeignKey('calendar.id'), nullable=False)
    calendar: Mapped[Calendar] = relationship("Calendar", back_populates="events")
    
    calendar_day_id: Mapped[Optional[int]] = mapped_column(ForeignKey('calendar_day.id'), nullable=False)
    calendar_day: Mapped[CalendarDay] = relationship("CalendarDay", back_populates="events")
