# resources/apiinfo.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/apiinfo

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ApiInfoResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "apiinfo"

    def version(self):
        # Note that this method only works if no authorization headers are present
        return self._call(f"{self.API_METHOD}.version", skip_auth=True)