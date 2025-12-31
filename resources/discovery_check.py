# resources/discovery_check.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/dcheck
try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class DiscoveryCheckResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "dcheck"

    def get(self, **filters):
        """
        Retrieve discovery checks according to the given parameters.
        
        Keyword Args (filters):
            dcheckids (list, optional): Return only discovery checks with the given IDs.
            druleids (list, optional): Return only discovery checks that belong to the given discovery rules.
            dserviceids (list, optional): Return only discovery checks that discovered the given discovered services.
            selectDRules (str|list, optional): Include discovery rules in the result.
            filter (dict, optional): Filter discovery checks by given properties.
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing discovery checks matching the criteria.
        
        Example:
            >>> # Get all discovery checks
            >>> discovery_checks = zapi.discovery_checks.get()
            >>> 
            >>> # Get discovery checks for a discovery rule
            >>> discovery_checks = zapi.discovery_checks.get(druleids=["1"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/dcheck/get
        """
        return self._call(f"{self.API_METHOD}.get", **filters)