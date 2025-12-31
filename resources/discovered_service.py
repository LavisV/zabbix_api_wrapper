# resources/discovered_service.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/dservice

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class DiscoveredServiceResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "dservice"

    def get(self, **filters):
        """
        Retrieve discovered services according to the given parameters.
        
        Keyword Args (filters):
            dserviceids (list, optional): Return only discovered services with the given IDs.
            dhostids (list, optional): Return only discovered services that belong to the given discovered hosts.
            dcheckids (list, optional): Return only discovered services discovered by the given discovery checks.
            druleids (list, optional): Return only discovered services discovered by the given discovery rules.
            selectDHosts (str|list, optional): Include discovered hosts in the result.
            selectDRules (str|list, optional): Include discovery rules in the result.
            filter (dict, optional): Filter discovered services by given properties.
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing discovered services matching the criteria.
        
        Example:
            >>> # Get all discovered services
            >>> discovered_services = zapi.discovered_services.get()
            >>> 
            >>> # Get discovered services for a discovered host
            >>> discovered_services = zapi.discovered_services.get(dhostids=["1"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/dservice/get
        """
        return self._call(f"{self.API_METHOD}.get", **filters)