from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship


class WalletTransaction(UUIDAuditBase):
    __tablename__ = "wallet_transaction"
    __table_args__ = {"comment": "Wallet Transaction for the application"}
    
    transaction_type: Mapped[str] = mapped_column(String(255), nullable=False, comment="Transaction type")
    transaction_amount: Mapped[float] = mapped_column(String(255), nullable=False, comment="Transaction amount")
    transaction_currency: Mapped[str] = mapped_column(String(255), nullable=False, comment="Transaction currency")
    transaction_date: Mapped[date] = mapped_column(Date, nullable=False, comment="Transaction date")
    transaction_comment: Mapped[str] = mapped_column(String(255), nullable=True, comment="Transaction comment")
    