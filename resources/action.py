# resources/action.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ActionResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)
    
    API_METHOD = "action"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, actionid):
        return self._call(f"{self.API_METHOD}.delete", actionids=[actionid])
    
    def get(self, actionid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", actionid=actionid, **filters)
    
    def massadd(self, **params):
        return self._call(f"{self.API_METHOD}.massadd", **params)