from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase
from datetime import datetime
from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

class CalendarYear(UUIDAuditBase):
    __tablename__ = "calendar_year"
    __table_args__ = {"comment": "Calendar year data used to track events and meetings"}
    
    calendar_year: Mapped[int] = mapped_column(Integer, nullable=False, comment="Calendar year")
    
    
    calendar_year_start_date: Mapped[datetime] = mapped_column(Date, nullable=False, comment="Start date of the calendar week")
    calendar_year_end_date: Mapped[datetime] = mapped_column(Date, nullable=False, comment="End date of the calendar week")

    