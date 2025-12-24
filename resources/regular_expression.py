# resources/regular_expression.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/regexp

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class RegularExpressionResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "regexp"

    def create(self, **params):
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, regexpid):
        return self._call(f"{self.API_METHOD}.delete", regexpid=regexpid)
    
    def get(self, regexpid=None, **filters):
        return self._call(f"{self.API_METHOD}.get", regexpid=regexpid, **filters)
    
    def update(self, regexpid, **params):
        return self._call(f"{self.API_METHOD}.update", regexpid=regexpid, **params)