from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .user import User
    
    
class Contact(UUIDAuditBase):
    '''The contact information for user/organization who can provide a service or is in some sense an asset to operations'''
    contact_title: Mapped[str] = mapped_column(String(50), nullable=True)
    contact_known_as: Mapped[str] = mapped_column(String(50), nullable=True)
    contact_description: Mapped[str] = mapped_column(String(5000), nullable=True)
    # contact name
    contact_first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    contact_middle_name: Mapped[str] = mapped_column(String(50), nullable=True)
    contact_last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    contact_purpose: Mapped[str] = mapped_column(String(5000), nullable=True)
    
    
    # contact information
    contact_telegram: Mapped[str] = mapped_column(String(50), nullable=True)
    contact_email: Mapped[str] = mapped_column(String(50), nullable=True)
    contact_tox: Mapped[str] = mapped_column(String(50), nullable=True)
    contact_xmpp: Mapped[str] = mapped_column(String(50), nullable=True)
    contact_phone: Mapped[str] = mapped_column(String(50), nullable=True)
    
    contact_registered_by: Mapped[User] = mapped_column(String(50), nullable=True)
    contact_registered_on: Mapped[date] = mapped_column(Date, nullable=True)
    
    
    
    
    
    
    