# resources/value_map.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/valuemap

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ValueMapResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "valuemap"
    
    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, valuemapid):
        return self._call(f"{self.API_METHOD}.delete", valuemapid=valuemapid)
    
    def get(self, valuemapid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", valuemapid=valuemapid, **filters)
    
    def update(self, valuemapid, **params):
        return self._call(f"{self.API_METHOD}.update", valuemapid=valuemapid, **params)