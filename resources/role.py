# resources/role.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class RoleResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "role"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, roleid):
        return self._call(f"{self.API_METHOD}.delete", roleid=roleid)
    
    def get(self, roleid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", roleid=roleid, **filters)
    
    def update(self, roleid, **params):
        return self._call(f"{self.API_METHOD}.update", roleid=roleid, **params)