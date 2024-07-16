from __future__ import annotations

from typing import Any, Dict, List, Union

from dotenv import load_dotenv
import os
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
load_dotenv()
class DatabaseConfig:
    
    DUCKDB_DATABASE_HOST: str = os.getenv("DUCKDB_DATABASE_HOST")
    DUCKDB_DATABASE_PORT: int = int(os.getenv("DUCKDB_DATABASE_PORT"))
    DUCKDB_DATABASE_NAME: str = os.getenv("DUCKDB_DATABASE_NAME")
    DUCKDB_DATABASE_USER: str = os.getenv("DUCKDB_DATABASE_USER")
    DUCKDB_DATABASE_PASSWORD: str = os.getenv("DUCKDB_DATABASE_PASSWORD")
    
    
class TorConfig:
    
    TOR_HOST: str = os.getenv("TOR_HOST")
    TOR_PORT: int = int(os.getenv("TOR_PORT"))
    TOR_PASSWORD: str = os.getenv("TOR_PASSWORD")
    TOR_USERNAME: str = os.getenv("TOR_USERNAME")
    TOR_SSL: bool = bool(os.getenv("TOR_SSL"))
    TOR_SSL_CERT: str = os.getenv("TOR_SSL_CERT")
    TOR_SSL_KEY: str = os.getenv("TOR_SSL_KEY")