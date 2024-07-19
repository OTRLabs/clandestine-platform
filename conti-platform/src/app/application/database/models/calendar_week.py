from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase
from datetime import datetime
from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CalendarWeek(UUIDAuditBase):
    __tablename__ = "calendar_week"
    __table_args__ = {"comment": "Calendar week data used to track events and meetings"}
    
    calendar_week: Mapped[int] = mapped_column(Integer, nullable=False, comment="Calendar week")
    
    calendar_week_start_date: Mapped[datetime] = mapped_column(Date, nullable=False, comment="Start date of the calendar week")
    calendar_week_end_date: Mapped[datetime] = mapped_column(Date, nullable=False, comment="End date of the calendar week")

    