from __future__ import annotations
from datetime import datetime, date
from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, Date, Integer, Boolean, Index, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


# This model represents the lifetime of a task, event, or C2 listener & more.
class Lifetime(UUIDAuditBase):
    
    start_date_time: Mapped[date] = mapped_column(Date, nullable=False, comment="Start date of the lifetime")
    startup_script: Mapped[str] = mapped_column(String, nullable=False, comment="Script to run on startup")
    shutdown_date_time: Mapped[date] = mapped_column(Date, nullable=False, comment="End date of the lifetime")
    shutdown_script: Mapped[str] = mapped_column(String, nullable=False, comment="Script to run on shutdown")
    
    # Additional fields
    name: Mapped[str] = mapped_column(String, nullable=False, comment="Name of the lifetime")
    description: Mapped[str] = mapped_column(String, nullable=True, comment="Description of the lifetime")
    status: Mapped[str] = mapped_column(String, nullable=False, comment="Status of the lifetime")
    priority: Mapped[int] = mapped_column(Integer, nullable=False, comment="Priority of the lifetime")
    duration: Mapped[int] = mapped_column(Integer, nullable=True, comment="Duration of the lifetime in minutes")
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, comment="Indicates if the lifetime is active")
