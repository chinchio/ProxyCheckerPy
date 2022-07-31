import requests
import json
from proxyProtocol import ProxyProtocol

class Proxy():
    def __init__(self, host: str, port: int, protocol: ProxyProtocol, auth: bool, username: str=None, password: str=None) -> None:
        self.host = host
        self.port = port
        self.protocol = protocol.value
        self.auth = auth
        self.username = username
        self.password = password

    def _proxy_uri(self) -> str:
        uri = ""
        if self.auth:
            uri = "{protocol}://{username}:{password}@{host}:{port}".format(
                protocol=self.protocol,
                username=self.username,
                password=self.password,
                host=self.host,
                port=self.port
            )
        else:
            uri = "{protocol}://{host}:{port}".format(
                protocol=self.protocol,
                host=self.host,
                port=self.port
            )
        return uri
    
    def check_available(self, timeout: int=20) -> bool:
        available = False
        proxies = {
            "https": self._proxy_uri()
        }
        try:
            r = requests.get("https://jsonip.com/", proxies = proxies, timeout=timeout)
            available = True
        except:
            available = False
        return available
    
    def __str__(self) -> str:
        st = {
            "host": self.host,
            "port": self.port,
            "protocol": self.protocol,
            "auth": self.auth
        }
        return f"<Proxy {str(json.dumps(st))}>"