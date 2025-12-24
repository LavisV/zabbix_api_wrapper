# resources/settings.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class SettingsResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "settings"

    def get(self, **params):
        return self._call(f"{self.API_METHOD}.get", **params)
    
    def update(self, **params):
        return self._call(f"{self.API_METHOD}.update", **params)