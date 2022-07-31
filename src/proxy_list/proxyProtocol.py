from enum import Enum

class ProxyProtocol(Enum):
    socks4 = "socks4"
    socks5 = "socks5"
    http = "http"
    https = "https"