# resources/apiinfo.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ApiInfoResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "apiinfo"

    def version(self, **filters):
        return self._call(f"{self.API_METHOD}.version", **filters)