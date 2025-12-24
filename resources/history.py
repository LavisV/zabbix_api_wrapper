# resources/history.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HistoryResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "history"

    def clear(self, **params):
        return self._call(f"{self.API_METHOD}.clear", **params)

    def get(self, **params):
        return self._call(f"{self.API_METHOD}.get", **params)

    def push(self, **params):
        return self._call(f"{self.API_METHOD}.push", **params)