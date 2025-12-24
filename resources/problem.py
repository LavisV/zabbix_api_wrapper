# resources/problem.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/problem

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ProblemResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "problem"

    def get(self, **params):
        return self._call(f"{self.API_METHOD}.get", **params)