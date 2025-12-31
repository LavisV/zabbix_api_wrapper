# resources/discovered_host.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/dhost

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class DiscoveredHostResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "dhost"

    def get(self, **filters):
        """
        Retrieve discovered hosts according to the given parameters.
        
        Keyword Args (filters):
            dhostids (list, optional): Return only discovered hosts with the given IDs.
            druleids (list, optional): Return only discovered hosts discovered by the given discovery rules.
            dserviceids (list, optional): Return only discovered hosts that have the given discovered services.
            selectDRules (str|list, optional): Include discovery rules in the result.
            selectDServices (str|list, optional): Include discovered services in the result.
            filter (dict, optional): Filter discovered hosts by given properties.
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing discovered hosts matching the criteria.
        
        Example:
            >>> # Get all discovered hosts
            >>> discovered_hosts = zapi.discovered_hosts.get()
            >>> 
            >>> # Get discovered hosts for a discovery rule
            >>> discovered_hosts = zapi.discovered_hosts.get(druleids=["1"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/dhost/get
        """
        return self._call(f"{self.API_METHOD}.get", **filters)