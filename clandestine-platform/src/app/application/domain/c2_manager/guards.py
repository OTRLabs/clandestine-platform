from __future__ import annotations

from typing import TYPE_CHECKING, Any

from typing import Any, Dict, List, Union
from litestar.exceptions import PermissionDeniedException

from ...config import constants
#from ...config.app import alchemy
from ...config.base import get_settings
from ...database.models import User
from ...domain.c2_manager import urls
if TYPE_CHECKING:
    from litestar.connection import ASGIConnection
    from litestar.handlers.base import BaseRouteHandler
    from litestar.security.jwt import Token


__all__ = ("requires_superuser", "requires_active_user", "requires_verified_user", "current_user_from_token", "auth")


settings = get_settings()