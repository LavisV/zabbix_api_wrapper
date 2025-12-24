# resources/host.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/host

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HostResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "host"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, hostid):
        return self._call(f"{self.API_METHOD}.delete", hostid=hostid)

    def get(self, hostid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", hostid=hostid, **filters)
    
    def massadd(self, **params):
        return self._call(f"{self.API_METHOD}.massadd", **params)

    def massremove(self, **params):
        return self._call(f"{self.API_METHOD}.massremove", **params)

    def massupdate(self, **params):
        return self._call(f"{self.API_METHOD}.massupdate", **params)

    def update(self, hostid, **params):
        return self._call(f"{self.API_METHOD}.update", hostid=hostid, **params)