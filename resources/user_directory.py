# resources/user_directory.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class UserDirectoryResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "userdirectory"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, userdirectoryid):
        return self._call(f"{self.API_METHOD}.delete", userdirectoryid=userdirectoryid)
    
    def get(self, userdirectoryid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", userdirectoryid=userdirectoryid, **filters)

    def test(self, **params):
        return self._call(f"{self.API_METHOD}.test", **params)
    
    def update(self, userdirectoryid, **params):
        return self._call(f"{self.API_METHOD}.update", userdirectoryid=userdirectoryid, **params)
