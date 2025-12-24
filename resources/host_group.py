# resources/host_group.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostgroup

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HostGroupResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "hostgroup"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, groupid):
        return self._call(f"{self.API_METHOD}.delete", groupid=groupid)
    
    def get(self, **params):
        return self._call(f"{self.API_METHOD}.get", **params)

    def massadd(self, **params):
            return self._call(f"{self.API_METHOD}.massadd", **params)

    def massremove(self, **params):
        return self._call(f"{self.API_METHOD}.massremove", **params)

    def massupdate(self, **params):
        return self._call(f"{self.API_METHOD}.massupdate", **params)

    def update(self, groupid, **params):
        return self._call(f"{self.API_METHOD}.update", groupid=groupid, **params)   