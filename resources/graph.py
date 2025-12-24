# resources/graph.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class GraphResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "graph"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, graphid):
        return self._call(f"{self.API_METHOD}.delete", graphid=graphid)
    
    def get(self, graphid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", graphid=graphid, **filters)
    
    def update(self, graphid, **params):
        return self._call(f"{self.API_METHOD}.update", graphid=graphid, **params)