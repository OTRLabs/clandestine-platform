from __future__ import annotations
from enum import Enum
from typing import Dict, List, Optional
from dataclasses import dataclass

class ProxyTypes(str, Enum):
    HTTP_PROXY = "HTTP_PROXY"
    HTTPS_PROXY = "HTTPS_PROXY"
    SOCKS4_PROXY = "SOCKS4_PROXY"
    SOCKS5_PROXY = "SOCKS5_PROXY"

@dataclass
class ServerConfig:
    hostname: str
    ip_address: str
    port: int
    username: Optional[str] = None
    password: Optional[str] = None

class ProjectInfrastructureHostTypes(str, Enum):
    """Project Infrastructure Host Types."""
    
    SMTP_SERVER = "SMTP_SERVER"
    DATABASE_SERVER = "DATABASE_SERVER"
    NETWORK_SCANNING_SERVER = "NETWORK_SCANNING_SERVER"
    PROXY_SERVER = "PROXY_SERVER"
    GIT_SERVER = "GIT_SERVER"
    S3_SERVER = "S3_SERVER"
    C2_SERVER = "C2_SERVER"
    PHISHING_SERVER = "PHISHING_SERVER"
    VPN_SERVER = "VPN_SERVER"
    EXPLOIT_SERVER = "EXPLOIT_SERVER"
    MALWARE_ANALYSIS_SERVER = "MALWARE_ANALYSIS_SERVER"

@dataclass
class Server:
    server_type: ProjectInfrastructureHostTypes
    config: ServerConfig
    description: str
    proxy_type: Optional[ProxyTypes] = None
    additional_info: Optional[Dict[str, str]] = None
