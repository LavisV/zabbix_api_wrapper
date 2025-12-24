# resources/item.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ItemResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)    

    API_METHOD = "item"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, itemid):
        return self._call(f"{self.API_METHOD}.delete", itemid=itemid)
    
    def get(self, itemid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", itemid=itemid, **filters)
    
    def update(self, itemid, **params):
        return self._call(f"{self.API_METHOD}.update", itemid=itemid, **params)