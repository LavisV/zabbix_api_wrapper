# resources/user.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class UserResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "user"

    def checkauthentication(self, **params):
        return self._call(f"{self.API_METHOD}.checkauthentication", **params)
    
    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, userid):
        return self._call(f"{self.API_METHOD}.delete", userid=userid)
    
    def get(self, userid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", userid=userid, **filters)

    def login(self, **params):
        return self._call(f"{self.API_METHOD}.login", **params)
    
    def logout(self, **params):
        return self._call(f"{self.API_METHOD}.logout", **params)

    def provision(self, **params):
        return self._call(f"{self.API_METHOD}.provision", **params)
    
    def reset_totp(self, **params):
        return self._call(f"{self.API_METHOD}.resettotp", **params)

    def unblock(self, **params):
        return self._call(f"{self.API_METHOD}.unblock", **params)
    
    def update(self, userid, **params):
        return self._call(f"{self.API_METHOD}.update", userid=userid, **params)