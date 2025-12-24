# resources/host_interface.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostinterface

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HostInterfaceResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "hostinterface"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, interfaceid):
        return self._call(f"{self.API_METHOD}.delete", interfaceid=interfaceid)
    
    def get(self, interfaceid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", interfaceid=interfaceid, **filters)

    def massadd(self, **params):
        return self._call(f"{self.API_METHOD}.massadd", **params)

    def massremove(self, **params):
        return self._call(f"{self.API_METHOD}.massremove", **params)

    def replacehostinterfaces(self, **params):
        return self._call(f"{self.API_METHOD}.replacehostinterfaces", **params)
    
    def update(self, interfaceid, **params):
        return self._call(f"{self.API_METHOD}.update", interfaceid=interfaceid, **params)