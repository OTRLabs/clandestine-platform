from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Event(UUIDAuditBase):
    __tablename__ = "event"
    __pii_columns__ = {"name", "description"}
    event_title: Mapped[str] = mapped_column(String(255), nullable=False, comment="Event title")
    event_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Event description")
    event_date: Mapped[datetime] = mapped_column(DateTime, nullable=False, comment="Event date")
    event_location: Mapped[str] = mapped_column(String(255), nullable=True, comment="Event location")
    event_data_url: Mapped[list[str]] = mapped_column(String(255), nullable=True, comment="Event data URL within the internal S3 bucket")
    
    