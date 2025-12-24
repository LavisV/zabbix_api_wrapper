# resources/configuration.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/configuration

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ConfigurationResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "configuration"

    def export(self, **filters):
        return self._call(f"{self.API_METHOD}.export", **filters)

    def import_configuration(self, **params): # import_configuration rather than import due to conflict with import keyword
        return self._call(f"{self.API_METHOD}.import", **params)

    def import_compare(self, **params):
        return self._call(f"{self.API_METHOD}.importcompare", **params)