# resources/correlation.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/correlation

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class CorrelationResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "correlation"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, correlationid):
        return self._call(f"{self.API_METHOD}.delete", correlationid=correlationid)
    
    def get(self, correlationid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", correlationid=correlationid, **filters)
    
    def update(self, correlationid, **params):
        return self._call(f"{self.API_METHOD}.update", correlationid=correlationid, **params)