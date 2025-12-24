# resources/auditlog.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/auditlog

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class AuditLogResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "auditlog"

    def get(self, **filters):
        return self._call(f"{self.API_METHOD}.get", **filters)