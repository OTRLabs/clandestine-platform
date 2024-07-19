from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional
from enum import Enum

class CommandNControlStatus(Enum, str):
    ACTIVE: str = "active"
    COMPROMISED: str = "compromised"
    INACTIVE: str = "inactive"
    DISABLED: str = "disabled"