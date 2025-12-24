# resources/housekeeping.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/housekeeping

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HousekeepingResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "housekeeping"

    def get(self, **params):
        return self._call(f"{self.API_METHOD}.get", **params)

    def run(self, **params):
        return self._call(f"{self.API_METHOD}.run", **params)