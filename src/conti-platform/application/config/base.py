
import binascii
import json
import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final

from advanced_alchemy.utils.text import slugify
from litestar.serialization import decode_json, encode_json
from litestar.utils.module_loader import module_to_os_path
#from redis.asyncio import Redis
from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.pool import NullPool

if TYPE_CHECKING:
    from litestar.data_extractors import RequestExtractorField, ResponseExtractorField

DEFAULT_MODULE_NAME = "app"
BASE_DIR: Final[Path] = module_to_os_path(DEFAULT_MODULE_NAME)

TRUE_VALUES = {"True", "true", "1", "yes", "Y", "T"}




class Settings:
    