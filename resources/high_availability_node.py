# resources/high_availability_node.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hanode

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HighAvailabilityNodeResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "hanode"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, highavailabilitynodeid):
        return self._call(f"{self.API_METHOD}.delete", highavailabilitynodeid=highavailabilitynodeid)
    
    def get(self, highavailabilitynodeid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", highavailabilitynodeid=highavailabilitynodeid, **filters)