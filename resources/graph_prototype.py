# resources/graph_prototype.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class GraphPrototypeResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "graphprototype"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, graphprototypeid):
        return self._call(f"{self.API_METHOD}.delete", graphprototypeid=graphprototypeid)
    
    def get(self, graphprototypeid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", graphprototypeid=graphprototypeid, **filters)

    def update(self, graphprototypeid, **params):
        return self._call(f"{self.API_METHOD}.update", graphprototypeid=graphprototypeid, **params)