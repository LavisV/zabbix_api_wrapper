# resources/user_group.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class UserGroupResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "usergroup"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, usergroupid):
        return self._call(f"{self.API_METHOD}.delete", usergroupid=usergroupid)
    
    def get(self, usergroupid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", usergroupid=usergroupid, **filters)
    
    def update(self, usergroupid, **params):
        return self._call(f"{self.API_METHOD}.update", usergroupid=usergroupid, **params)