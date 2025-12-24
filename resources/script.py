# resources/script.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ScriptResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "script"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, scriptid):
        return self._call(f"{self.API_METHOD}.delete", scriptid=scriptid)

    def execute(self, scriptid, **params):
        return self._call(f"{self.API_METHOD}.execute", scriptid=scriptid, **params)
    
    def get(self, scriptid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", scriptid=scriptid, **filters)

    def get_scripts_by_events(self, **params):
        return self._call(f"{self.API_METHOD}.getscriptsbyevents", **params)
    
    def get_scripts_by_hosts(self, **params):
        return self._call(f"{self.API_METHOD}.getscriptsbyshosts", **params)
        
    def update(self, scriptid, **params):
        return self._call(f"{self.API_METHOD}.update", scriptid=scriptid, **params)