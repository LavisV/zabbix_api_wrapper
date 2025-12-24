# resources/discovery_check.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/dcheck
try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class DiscoveryCheckResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "dcheck"

    def get(self, **filters):
        return self._call(f"{self.API_METHOD}.get", **filters)