from __future__ import annotations

from datetime import datetime, date

from typing import TYPE_CHECKING, List, Optional
from advanced_alchemy.base import UUIDAuditBase

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .wallet_transaction import WalletTransaction
    from .user import User
    from .wallet_currencies import WalletCurrencies
class Wallet(UUIDAuditBase):
    '''A Crypto Wallet for the application'''
    __tablename__ = "wallet"
    __table_args__ = {"comment": "Wallet for the application"}
    
    wallet_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Wallet name")
    wallet_description: Mapped[str] = mapped_column(String(255), nullable=False, comment="Wallet description")
    wallet_currency: Mapped[WalletCurrencies] = mapped_column(String(255), nullable=False, comment="Wallet currency")
    wallet_balance: Mapped[float] = mapped_column(String(255), nullable=False, comment="Wallet balance")
    wallet_value: Mapped[float] = mapped_column(String(255), nullable=False, comment="Wallet value in USD")
    wallet_owner: Mapped[User] = relationship("User", back_populates="wallet", uselist=False, lazy="joined")
    wallet_transactions: Mapped[list[WalletTransaction]] = relationship("Transaction", back_populates="wallet", uselist=True, lazy="joined")
    