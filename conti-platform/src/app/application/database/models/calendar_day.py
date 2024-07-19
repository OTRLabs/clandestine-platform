from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase
from datetime import datetime
from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship



class CalendarDay(UUIDAuditBase):
    __tablename__ = "calendar_day"
    __table_args__ = {"comment": "Calendar day data used to track events and meetings"}
    
    calendar_day: Mapped[int] = mapped_column(Integer, nullable=False, comment="Calendar day")
    
    calendar_day_date: Mapped[datetime] = mapped_column(Date, nullable=False, comment="Date of the calendar day")
    
    