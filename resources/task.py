# resources/task.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/task

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TaskResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "task"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)

    def get(self, **params):
        return self._call(f"{self.API_METHOD}.get", **params)