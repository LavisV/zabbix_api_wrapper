# resources/proxy_group.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ProxyGroupResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "proxygroup"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, proxygroupid):
        return self._call(f"{self.API_METHOD}.delete", proxygroupid=proxygroupid)
    
    def get(self, proxygroupid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", proxygroupid=proxygroupid, **filters)
    
    def update(self, proxygroupid, **params):
        return self._call(f"{self.API_METHOD}.update", proxygroupid=proxygroupid, **params)