# resources/template_dashboard.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templatedashboard

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TemplateDashboardResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "templatedashboard"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, templatedashboardid):
        return self._call(f"{self.API_METHOD}.delete", templatedashboardid=templatedashboardid)
    
    def get(self, templatedashboardid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", templatedashboardid=templatedashboardid, **filters)
    
    def update(self, templatedashboardid, **params):
        return self._call(f"{self.API_METHOD}.update", templatedashboardid=templatedashboardid, **params)