# resources/maintenance.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class MaintenanceResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "maintenance"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, maintenanceid):
        return self._call(f"{self.API_METHOD}.delete", maintenanceid=maintenanceid)
    
    def get(self, maintenanceid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", maintenanceid=maintenanceid, **filters)
    
    def update(self, maintenanceid, **params):
        return self._call(f"{self.API_METHOD}.update", maintenanceid=maintenanceid, **params)