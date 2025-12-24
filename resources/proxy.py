# resources/proxy.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ProxyResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "proxy"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, proxyid):
        return self._call(f"{self.API_METHOD}.delete", proxyid=proxyid)
    
    def get(self, proxyid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", proxyid=proxyid, **filters)
    
    def update(self, proxyid, **params):
        return self._call(f"{self.API_METHOD}.update", proxyid=proxyid, **params)