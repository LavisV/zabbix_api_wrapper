# resources/module.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/module

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ModuleResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "module"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)

    def delete(self, moduleid):
        return self._call(f"{self.API_METHOD}.delete", moduleid=moduleid)
    
    def get(self, moduleid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", moduleid=moduleid, **filters)
    
    def update(self, moduleid, **params):
        return self._call(f"{self.API_METHOD}.update", moduleid=moduleid, **params)