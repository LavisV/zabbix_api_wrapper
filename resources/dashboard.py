# resources/dashboard.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class DashboardResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "dashboard"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, dashboardid):
        return self._call(f"{self.API_METHOD}.delete", dashboardid=dashboardid)
    
    def get(self, dashboardid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", dashboardid=dashboardid, **filters)
    
    def update(self, dashboardid, **params):
        return self._call(f"{self.API_METHOD}.update", dashboardid=dashboardid, **params)