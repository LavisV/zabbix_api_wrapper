# resources/item_prototype.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/itemprototype

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ItemPrototypeResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "itemprototype"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, itemprototypeid):
        return self._call(f"{self.API_METHOD}.delete", itemprototypeid=itemprototypeid)
    
    def get(self, itemprototypeid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", itemprototypeid=itemprototypeid, **filters)
    
    def update(self, itemprototypeid, **params):
        return self._call(f"{self.API_METHOD}.update", itemprototypeid=itemprototypeid, **params)