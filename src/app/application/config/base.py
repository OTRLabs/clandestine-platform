
import binascii
import json
import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING, Any

from advanced_alchemy.utils.text import slugify
from litestar.serialization import decode_json, encode_json
from litestar.utils.module_loader import module_to_os_path
#from redis.asyncio import Redis
from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.pool import NullPool
from .env_vars import DatabaseConfig, TorConfig
if TYPE_CHECKING:
    from litestar.data_extractors import RequestExtractorField, ResponseExtractorField





class Settings:
    
    #app: str = "app"
    database: DatabaseConfig = DatabaseConfig()
    tor_service: TorConfig = TorConfig()
    
def get_settings() -> Settings:
    return Settings()