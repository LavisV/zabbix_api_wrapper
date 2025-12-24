# resources/mfa.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class MFAResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "mfa"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, mfaid):
        return self._call(f"{self.API_METHOD}.delete", mfaid=mfaid)
    
    def get(self, mfaid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", mfaid=mfaid, **filters)
    
    def update(self, mfaid, **params):
        return self._call(f"{self.API_METHOD}.update", mfaid=mfaid, **params)