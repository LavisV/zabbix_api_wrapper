# resources/user_macro.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class UserMacroResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "usermacro"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)

    def create_global(self, **params):
        return self._call(f"{self.API_METHOD}.createglobal", **params)
    
    def delete(self, usermacroid):
        return self._call(f"{self.API_METHOD}.delete", usermacroid=usermacroid)

    def delete_global(self, **params):
        return self._call(f"{self.API_METHOD}.deleteglobal", **params)
    
    def get(self, **params):
        return self._call(f"{self.API_METHOD}.get", **params)
    
    def update(self, **params):
        return self._call(f"{self.API_METHOD}.update", **params)
    
    def update_global(self, **params):
        return self._call(f"{self.API_METHOD}.updateglobal", **params)