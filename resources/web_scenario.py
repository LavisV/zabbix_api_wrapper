# resources/web_scenario.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class WebScenarioResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "httptest"
    
    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, httptestid):
        return self._call(f"{self.API_METHOD}.delete", httptestid=httptestid)
    
    def get(self, httptestid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", httptestid=httptestid, **filters)
    
    def update(self, httptestid, **params):
        return self._call(f"{self.API_METHOD}.update", httptestid=httptestid, **params)