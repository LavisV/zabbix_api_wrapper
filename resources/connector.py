# resources/connector.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ConnectorResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "connector"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, connectorid):
        return self._call(f"{self.API_METHOD}.delete", connectorid=connectorid)
    
    def get(self, connectorid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", connectorid=connectorid, **filters)
    
    def update(self, connectorid, **params):
        return self._call(f"{self.API_METHOD}.update", connectorid=connectorid, **params)