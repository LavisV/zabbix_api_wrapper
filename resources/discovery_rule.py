# resources/discovery_rule.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/drule

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class DiscoveryRuleResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "drule"

    def create(self, **params):
        """
        Create new network discovery rules.
        
        Keyword Args (params):
            name (str, required): Name of the discovery rule.
            iprange (str, required): IP address range to scan (e.g., "192.168.1.1-255").
            delay (str, required): Update interval of the discovery rule.
            proxy_hostid (str, optional): ID of the proxy used for discovery.
            dchecks (list, required): Discovery checks. Each object should contain type, ports, key_, snmp_community, snmpv3_securityname, snmpv3_securitylevel, snmpv3_authpassphrase, snmpv3_privpassphrase, snmpv3_authprotocol, snmpv3_privprotocol, uniq, host_source, name_source.
            status (int, optional): Whether the discovery rule is enabled (0: enabled, 1: disabled).
            description (str, optional): Description of the discovery rule.
        
        Returns:
            dict: API response containing the IDs of created discovery rules.
        
        Example:
            >>> discovery_rule = zapi.discovery_rules.create(
            ...     name="Network Discovery",
            ...     iprange="192.168.1.1-255",
            ...     delay="1h",
            ...     dchecks=[{
            ...         "type": 9,
            ...         "ports": "161",
            ...         "snmp_community": "public"
            ...     }]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/drule/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, droleid):
        """
        Delete network discovery rules.
        
        Args:
            droleid (str|list): ID or list of IDs of discovery rules to delete.
        
        Returns:
            dict: API response containing the IDs of deleted discovery rules.
        
        Example:
            >>> # Delete a single discovery rule
            >>> zapi.discovery_rules.delete(droleid="1")
            >>> 
            >>> # Delete multiple discovery rules
            >>> zapi.discovery_rules.delete(droleid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/drule/delete
        """
        return self._call(f"{self.API_METHOD}.delete", droleid=droleid)

    def get(self, droleid=None, **filters):
        """
        Retrieve network discovery rules according to the given parameters.
        
        Args:
            droleid (str|list, optional): Return only discovery rules with the given IDs.
            
        Keyword Args (filters):
            selectDChecks (str|list, optional): Include discovery checks in the result.
            selectDHosts (str|list, optional): Include discovered hosts in the result.
            filter (dict, optional): Filter discovery rules by given properties.
            search (dict, optional): Search discovery rules by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing discovery rules matching the criteria.
        
        Example:
            >>> # Get all discovery rules
            >>> discovery_rules = zapi.discovery_rules.get()
            >>> 
            >>> # Get discovery rule with checks
            >>> discovery_rule = zapi.discovery_rules.get(droleid="1", selectDChecks="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/drule/get
        """
        return self._call(f"{self.API_METHOD}.get", droleid=droleid, **filters)
    
    def update(self, droleid, **params):
        """
        Update existing network discovery rules.
        
        Args:
            droleid (str): ID of the discovery rule to update.
            
        Keyword Args (params):
            name (str, optional): Name of the discovery rule.
            iprange (str, optional): IP address range to scan.
            delay (str, optional): Update interval of the discovery rule.
            proxy_hostid (str, optional): ID of the proxy used for discovery.
            dchecks (list, optional): Discovery checks.
            status (int, optional): Whether the discovery rule is enabled (0: enabled, 1: disabled).
            description (str, optional): Description of the discovery rule.
        
        Returns:
            dict: API response containing the IDs of updated discovery rules.
        
        Example:
            >>> zapi.discovery_rules.update(
            ...     droleid="1",
            ...     name="Updated Discovery Rule Name",
            ...     status=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/drule/update
        """
        return self._call(f"{self.API_METHOD}.update", droleid=droleid, **params)