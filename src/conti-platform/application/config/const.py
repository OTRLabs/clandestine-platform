from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING
import binascii
import json
import os


if TYPE_CHECKING:
    from litestar.data_extractors import RequestExtractorField, ResponseExtractorField

DEFAULT_MODULE_NAME = "app"
BASE_DIR: str = "/"
TRUE_VALUES = {"True", "true", "1", "yes", "Y", "T"}
ROOT_ROUTE: str = '/'
APP_ROUTE: str = '/app'
API_ROUTES: str = '/api'

