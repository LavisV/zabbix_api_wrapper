# base.py

# Abstract class with common functionality
# Has reference to parent Zabbix API client, ZabbixClient
# Contains _call() method that delegates to the client's _request() method

class ZabbixBase:
    def __init__(self, client):
        self._client = client

    def _call(self, method, skip_auth=False, **params):
        # Delegate to the client's _request() method
        return self._client._request(method, params, skip_auth=skip_auth)