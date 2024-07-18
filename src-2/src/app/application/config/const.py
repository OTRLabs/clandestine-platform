from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING, Final
import binascii
import json
import os
from litestar.utils.module_loader import module_to_os_path

if TYPE_CHECKING:
    from litestar.data_extractors import RequestExtractorField, ResponseExtractorField


DEFAULT_MODULE_NAME = "conti-platform"
BASE_DIR: Final[Path] = module_to_os_path(DEFAULT_MODULE_NAME)
BASE_DIR: str = "/"
TRUE_VALUES = {"True", "true", "1", "yes", "Y", "T"}
ROOT_ROUTE: str = '/'
APP_ROUTE: str = '/app'
API_ROUTES: str = '/api'

TRUE_VALUES = {"True", "true", "1", "yes", "Y", "T"}


DEFAULT_USER_ROLE: str = "member"