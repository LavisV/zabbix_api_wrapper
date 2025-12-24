# resources/map.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/map

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class MapResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "map"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, mapid):
        return self._call(f"{self.API_METHOD}.delete", mapid=mapid)
    
    def get(self, mapid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", mapid=mapid, **filters)
    
    def update(self, mapid, **params):
        return self._call(f"{self.API_METHOD}.update", mapid=mapid, **params)