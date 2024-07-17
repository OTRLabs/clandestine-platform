from __future__ import annotations

from enum import Enum


class WalletCurrencies(str, Enum):
    
    BTC: str = "BTC"
    XMR: str = "XMR"
    