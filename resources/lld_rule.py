# resources/lld_rule.py

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class LLDRuleResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "discoveryrule"

    def copy(self, droleid, **params):
        return self._call(f"{self.API_METHOD}.copy", droleid=droleid, **params)
    
    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, droleid):
        return self._call(f"{self.API_METHOD}.delete", droleid=droleid)
    
    def get(self, droleid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", droleid=droleid, **filters)
    
    def update(self, droleid, **params):
        return self._call(f"{self.API_METHOD}.update", droleid=droleid, **params)