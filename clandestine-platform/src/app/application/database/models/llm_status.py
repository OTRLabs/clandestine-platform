from __future__ import annotations

from enum import Enum

class LargeLanguageModelStatus(Enum, str):
    ACTIVE: str = "ACTIVE"
    INACTIVE: str = "INACTIVE"
    READING: str = "READING"
    THINKING: str = "THINKING"
    PENDING: str = "PENDING"
    ERROR: str = "ERROR"
    DELETED: str = "DELETED"
    UNKNOWN: str = "UNKNOWN"
    NOT_APPLICABLE: str = "NOT_APPLICABLE"
    NOT_AVAILABLE: str = "NOT_AVAILABLE"
    NOT_SUPPORTED: str = "NOT_SUPPORTED"
    NOT_IMPLEMENTED: str = "NOT_IMPLEMENTED"
    NOT_CONFIGURED: str = "NOT_CONFIGURED"
    NOT_AUTHORIZED: str = "NOT_AUTHORIZED"
    NOT_FOUND: str = "NOT_FOUND"
    NOT_ALLOWED: str = "NOT_ALLOWED"
    NOT_ACCEPTED: str = "NOT_ACCEPTED"
    NOT_SUPPORTED: str = "NOT_SUPPORTED"
    NOT_AVAILABLE: str = "NOT_AVAILABLE"
    TIMED_OUT: str = "TIMED_OUT"