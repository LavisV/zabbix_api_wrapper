# resources/sla.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class SLAResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "sla"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, slaid):
        return self._call(f"{self.API_METHOD}.delete", slaid=slaid)
    
    def get(self, slaid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", slaid=slaid, **filters)

    def get_sli(self, **params):
        return self._call(f"{self.API_METHOD}.getsli", **params)
