from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Report(UUIDAuditBase):
    '''reports on a series of events or actions preformed by the platform'''
    __tablename__ = "report"
    __table_args__ = {"comment": "Reports on a series of events or actions preformed by the platform"}
    
    report_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Report name")
    report_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Report description")
    report_data: Mapped[str] = mapped_column(String(255), nullable=False, comment="Report data")
    report_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Report date")
    report_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, comment="Report time")
    