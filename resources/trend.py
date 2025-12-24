# resources/trend.py

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