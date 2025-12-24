# resources/trigger.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/trigger

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TriggerResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "trigger"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, triggerid):
        return self._call(f"{self.API_METHOD}.delete", triggerid=triggerid)
    
    def get(self, triggerid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", triggerid=triggerid, **filters)
    
    def update(self, triggerid, **params):
        return self._call(f"{self.API_METHOD}.update", triggerid=triggerid, **params)