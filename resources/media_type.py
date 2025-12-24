# resources/media_type.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class MediaTypeResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "mediatype"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, mediatypeid):
        return self._call(f"{self.API_METHOD}.delete", mediatypeid=mediatypeid)
    
    def get(self, mediatypeid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", mediatypeid=mediatypeid, **filters)
    
    def update(self, mediatypeid, **params):
        return self._call(f"{self.API_METHOD}.update", mediatypeid=mediatypeid, **params)