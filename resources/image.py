# resources/image.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/image

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ImageResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "image"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, imageid):
        return self._call(f"{self.API_METHOD}.delete", imageid=imageid)
    
    def get(self, imageid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", imageid=imageid, **filters)
        
    def update(self, imageid, **params):
        return self._call(f"{self.API_METHOD}.update", imageid=imageid, **params)