# resources/report.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/report

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ReportResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "report"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, reportid):
        return self._call(f"{self.API_METHOD}.delete", reportid=reportid)
    
    def get(self, reportid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", reportid=reportid, **filters)
    
    def update(self, reportid, **params):
        return self._call(f"{self.API_METHOD}.update", reportid=reportid, **params)