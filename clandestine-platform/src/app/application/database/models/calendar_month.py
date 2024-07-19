from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase
from datetime import datetime
from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CalendarMonth(UUIDAuditBase):
    __tablename__ = "calendar_month"
    __table_args__ = {"comment": "Calendar month data used to track events and meetings"}
    
    calendar_month: Mapped[int] = mapped_column(Integer, nullable=False, comment="Calendar month")
    
    calendar_month_start_date: Mapped[datetime] = mapped_column(Date, nullable=False, comment="Start date of the calendar month")
    calendar_month_end_date: Mapped[datetime] = mapped_column(Date, nullable=False, comment="End date of the calendar month")