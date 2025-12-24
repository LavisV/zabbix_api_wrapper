# resources/trend.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/trend

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TrendResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "trend"
    
    def get(self, **params):
        return self._call(f"{self.API_METHOD}.get", **params)