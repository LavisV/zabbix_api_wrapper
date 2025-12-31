# resources/housekeeping.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/housekeeping

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HousekeepingResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "housekeeping"

    def get(self, **params):
        """
        Get housekeeping settings.
        
        Keyword Args (params):
            (No parameters required)
        
        Returns:
            dict: API response containing housekeeping settings.
        
        Example:
            >>> housekeeping_settings = zapi.housekeeping.get()
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/housekeeping/get
        """
        return self._call(f"{self.API_METHOD}.get", **params)

    def run(self, **params):
        """
        Run housekeeping manually.
        
        Keyword Args (params):
            (No parameters required)
        
        Returns:
            dict: API response confirming housekeeping execution.
        
        Example:
            >>> zapi.housekeeping.run()
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/housekeeping/run
        """
        return self._call(f"{self.API_METHOD}.run", **params)