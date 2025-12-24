# resources/discovered_host.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/dhost

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