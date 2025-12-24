# resources/trigger_prototype.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TriggerPrototypeResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "triggerprototype"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, triggerprototypeid):
        return self._call(f"{self.API_METHOD}.delete", triggerprototypeid=triggerprototypeid)
    
    def get(self, triggerprototypeid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", triggerprototypeid=triggerprototypeid, **filters)
    
    def update(self, triggerprototypeid, **params):
        return self._call(f"{self.API_METHOD}.update", triggerprototypeid=triggerprototypeid, **params)