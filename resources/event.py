# resources/event.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/event

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class EventResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "event"

    def get(self, **filters):
        return self._call(f"{self.API_METHOD}.get", **filters)
    
    def acknowledge(self, **params):
        return self._call(f"{self.API_METHOD}.acknowledge", **params)