# resources/token.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TokenResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "token"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, tokenid):
        return self._call(f"{self.API_METHOD}.delete", tokenid=tokenid)
    
    def generate(self, **params):
        return self._call(f"{self.API_METHOD}.generate", **params)

    def get(self, tokenid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", tokenid=tokenid, **filters)
      
    def update(self, tokenid, **params):
        return self._call(f"{self.API_METHOD}.update", tokenid=tokenid, **params)