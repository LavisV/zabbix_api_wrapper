# resources/template.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/template

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TemplateResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "template"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, templateid):
        return self._call(f"{self.API_METHOD}.delete", templateid=templateid)
    
    def get(self, templateid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", templateid=templateid, **filters)

    def mass_add(self, **params):
        return self._call(f"{self.API_METHOD}.massadd", **params)

    def mass_remove(self, **params):
        return self._call(f"{self.API_METHOD}.massremove", **params)

    def mass_update(self, **params):
        return self._call(f"{self.API_METHOD}.massupdate", **params)
    
    def update(self, templateid, **params):
        return self._call(f"{self.API_METHOD}.update", templateid=templateid, **params)