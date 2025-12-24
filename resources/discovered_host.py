# resources/discovered_host.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class DiscoveredHostResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "dhost"

    def get(self, **filters):
        return self._call(f"{self.API_METHOD}.get", **filters)