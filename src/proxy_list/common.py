import requests
from proxy import Proxy

class Base():
    def __init__(self, proxy_list_uri: str) -> None:
        self.proxy_list_uri = proxy_list_uri
        self.req = self._crawler()
        self.proxies = self._parse()

    def _crawler(self) -> requests.models.Response:
        r = requests.get(self.proxy_list_uri)
        return r

    def _parse(self):
        pass

    def get_proxies(self) -> list[Proxy]:
        return self.proxies

class Source():
    pass