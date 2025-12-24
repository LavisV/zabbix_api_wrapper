# resources/authentication.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/authentication
try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class AuthenticationResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "authentication"

    def get(self, **params):
        return self._call(f"{self.API_METHOD}.get", **params)

    def update(self, **params):
        return self._call(f"{self.API_METHOD}.update", **params)