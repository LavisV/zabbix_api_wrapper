# resources/icon_map.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class IconMapResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "iconmap"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, iconmapid):
        return self._call(f"{self.API_METHOD}.delete", iconmapid=iconmapid)
    
    def get(self, iconmapid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", iconmapid=iconmapid, **filters)
    
    def update(self, iconmapid, **params):
        return self._call(f"{self.API_METHOD}.update", iconmapid=iconmapid, **params)