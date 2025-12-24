# resources/graph_item.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graphitem

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class GraphItemResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "graphitem"

    def get(self, **filters):
        return self._call(f"{self.API_METHOD}.get", **filters)