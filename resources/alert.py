# resources/alert.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class AlertResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "alert"

    def get(self, alertid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", alertid=alertid, **filters)