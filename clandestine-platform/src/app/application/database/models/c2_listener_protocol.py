from __future__ import annotations

from enum import Enum
class CommandNControlListenerProtocol(Enum, str):
    HTTP: str = "HTTP"
    HTTPS: str = "HTTPS"
    HTTP_TOR: str = "HTTP_TOR"
    HTTPS_TOR: str = "HTTPS_TOR"
    DNS: str = "DNS"
    DNS_TOR: str = "DNS_TOR"
    NOISE: str = "NOISE"
    SMTP: str = "SMTP"
    FTP: str = "FTP"
    SSH: str = "SSH"