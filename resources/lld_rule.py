# resources/lld_rule.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class LLDRuleResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "discoveryrule"

    def copy(self, droleid, **params):
        """
        Copy low-level discovery rules.
        
        Args:
            droleid (str): ID of the LLD rule to copy.
            
        Keyword Args (params):
            discoveryids (list, required): IDs of LLD rules to create copies for.
        
        Returns:
            dict: API response containing the IDs of copied LLD rules.
        
        Example:
            >>> zapi.lld_rules.copy(
            ...     droleid="1",
            ...     discoveryids=["1"]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/copy
        """
        return self._call(f"{self.API_METHOD}.copy", droleid=droleid, **params)
    
    def create(self, **params):
        """
        Create new low-level discovery rules.
        
        Keyword Args (params):
            name (str, required): Name of the LLD rule.
            key_ (str, required): Item key of the LLD rule.
            hostid (str, required): ID of the host that the LLD rule belongs to.
            type (int, required): Type of the LLD rule (see Zabbix documentation for type values).
            interfaceid (str, optional): ID of the item's host interface.
            delay (str, optional): Update interval of the LLD rule.
            lifetime (int, optional): Time in days to keep discovered resources (0: forever).
            description (str, optional): Description of the LLD rule.
            status (int, optional): Whether the LLD rule is enabled (0: enabled, 1: disabled).
            parameters (dict, optional): Item-specific parameters.
            preprocessing (list, optional): Preprocessing options.
            filter (dict, optional): Discovery rule filter.
            lld_macro_paths (list, optional): LLD macro paths.
            overrides (list, optional): LLD rule overrides.
            tags (list, optional): LLD rule tags.
        
        Returns:
            dict: API response containing the IDs of created LLD rules.
        
        Example:
            >>> lld_rule = zapi.lld_rules.create(
            ...     name="Filesystem Discovery",
            ...     key_="vfs.fs.discovery",
            ...     hostid="10105",
            ...     type=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, droleid):
        """
        Delete low-level discovery rules.
        
        Args:
            droleid (str|list): ID or list of IDs of LLD rules to delete.
        
        Returns:
            dict: API response containing the IDs of deleted LLD rules.
        
        Example:
            >>> # Delete a single LLD rule
            >>> zapi.lld_rules.delete(droleid="1")
            >>> 
            >>> # Delete multiple LLD rules
            >>> zapi.lld_rules.delete(droleid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/delete
        """
        return self._call(f"{self.API_METHOD}.delete", droleid=droleid)

    def get(self, droleid=None, **filters):
        """
        Retrieve low-level discovery rules according to the given parameters.
        
        Args:
            droleid (str|list, optional): Return only LLD rules with the given IDs.
            
        Keyword Args (filters):
            itemids (list, optional): Return only LLD rules with the given item IDs (alias for droleid).
            hostids (list, optional): Return only LLD rules that belong to the given hosts.
            groupids (list, optional): Return only LLD rules that belong to hosts in the given host groups.
            templateids (list, optional): Return only LLD rules that belong to the given templates.
            inherited (bool, optional): Return only inherited LLD rules.
            templated (bool, optional): Return only LLD rules that belong to templates.
            monitored (bool, optional): Return only enabled LLD rules that belong to monitored hosts.
            selectHosts (str|list, optional): Include hosts in the result.
            selectItems (str|list, optional): Include items in the result.
            selectTriggers (str|list, optional): Include triggers in the result.
            selectGraphs (str|list, optional): Include graphs in the result.
            selectHostPrototypes (str|list, optional): Include host prototypes in the result.
            selectItemPrototypes (str|list, optional): Include item prototypes in the result.
            selectTriggerPrototypes (str|list, optional): Include trigger prototypes in the result.
            selectGraphPrototypes (str|list, optional): Include graph prototypes in the result.
            selectFilter (str|list, optional): Include filter in the result.
            selectPreprocessing (str|list, optional): Include preprocessing options in the result.
            selectOverrides (str|list, optional): Include overrides in the result.
            selectTags (str|list, optional): Include tags in the result.
            filter (dict, optional): Filter LLD rules by given properties.
            search (dict, optional): Search LLD rules by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing LLD rules matching the criteria.
        
        Example:
            >>> # Get all LLD rules
            >>> lld_rules = zapi.lld_rules.get()
            >>> 
            >>> # Get LLD rules for a host
            >>> lld_rules = zapi.lld_rules.get(hostids=["10105"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/get
        """
        return self._call(f"{self.API_METHOD}.get", droleid=droleid, **filters)
    
    def update(self, droleid, **params):
        """
        Update existing low-level discovery rules.
        
        Args:
            droleid (str): ID of the LLD rule to update.
            
        Keyword Args (params):
            name (str, optional): Name of the LLD rule.
            key_ (str, optional): Item key of the LLD rule.
            hostid (str, optional): ID of the host that the LLD rule belongs to.
            type (int, optional): Type of the LLD rule.
            interfaceid (str, optional): ID of the item's host interface.
            delay (str, optional): Update interval of the LLD rule.
            lifetime (int, optional): Time in days to keep discovered resources (0: forever).
            description (str, optional): Description of the LLD rule.
            status (int, optional): Whether the LLD rule is enabled (0: enabled, 1: disabled).
            parameters (dict, optional): Item-specific parameters.
            preprocessing (list, optional): Preprocessing options.
            filter (dict, optional): Discovery rule filter.
            lld_macro_paths (list, optional): LLD macro paths.
            overrides (list, optional): LLD rule overrides.
            tags (list, optional): LLD rule tags.
        
        Returns:
            dict: API response containing the IDs of updated LLD rules.
        
        Example:
            >>> zapi.lld_rules.update(
            ...     droleid="1",
            ...     status=1,
            ...     delay="5m"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/update
        """
        return self._call(f"{self.API_METHOD}.update", droleid=droleid, **params)