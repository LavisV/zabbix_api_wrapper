# resources/host_prototype.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HostPrototypeResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "hostprototype"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, hostprototypeid):
        return self._call(f"{self.API_METHOD}.delete", hostprototypeid=hostprototypeid)
    
    def get(self, hostprototypeid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", hostprototypeid=hostprototypeid, **filters)
    
    def update(self, hostprototypeid, **params):
        return self._call(f"{self.API_METHOD}.update", hostprototypeid=hostprototypeid, **params)