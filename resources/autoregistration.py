# resources/autoregistration.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class AutoRegistrationResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "autoregistration"

    def get(self, **filters):
        return self._call(f"{self.API_METHOD}.get", **filters)

    def update(self, **params):
        return self._call(f"{self.API_METHOD}.update", **params)