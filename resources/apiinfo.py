# resources/apiinfo.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/apiinfo

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ApiInfoResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "apiinfo"

    def version(self):
        """
        Get Zabbix API version.
        
        Note: This method only works if no authorization headers are present.
        
        Returns:
            dict: API response containing the Zabbix API version string.
        
        Example:
            >>> version = zapi.apiinfo.version()
            >>> print(version["result"])
            "7.0.0"
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/apiinfo/version
        """
        return self._call(f"{self.API_METHOD}.version", skip_auth=True)