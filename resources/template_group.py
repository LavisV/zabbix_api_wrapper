# resources/template_group.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templategroup

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TemplateGroupResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "templategroup"
    
    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, templategroupid):
        return self._call(f"{self.API_METHOD}.delete", templategroupid=templategroupid)
    
    def get(self, templategroupid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", templategroupid=templategroupid, **filters)

    def mass_add(self, **params):
        return self._call(f"{self.API_METHOD}.massadd", **params)

    def mass_remove(self, **params):
        return self._call(f"{self.API_METHOD}.massremove", **params)

    def mass_update(self, **params):
        return self._call(f"{self.API_METHOD}.massupdate", **params)

    def propagate(self, **params):
        return self._call(f"{self.API_METHOD}.propagate", **params)
    
    def update(self, templategroupid, **params):
        return self._call(f"{self.API_METHOD}.update", templategroupid=templategroupid, **params)