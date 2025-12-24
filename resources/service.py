# resources/service.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ServiceResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "service"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, serviceid):
        return self._call(f"{self.API_METHOD}.delete", serviceid=serviceid)
    
    def get(self, serviceid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", serviceid=serviceid, **filters)
    
    def update(self, serviceid, **params):
        return self._call(f"{self.API_METHOD}.update", serviceid=serviceid, **params)