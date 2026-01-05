# resources/proxy_group.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/proxygroup

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ProxyGroupResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "proxygroup"

    def create(self, **params):
        """
        Create new proxy groups.
        
        Keyword Args (params):
            name (str, required): Name of the proxy group.
            failover_delay (int, optional): Failover delay in seconds.
            min_online (int, optional): Minimum number of online proxies in the group.
        
        Returns:
            dict: API response containing the IDs of created proxy groups.
        
        Example:
            >>> proxy_group = zapi.proxy_groups.create(
            ...     name="Primary Proxy Group",
            ...     failover_delay=60,
            ...     min_online=1
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/proxygroup/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, proxygroupid):
        """
        Delete proxy groups.
        
        Args:
            proxygroupid (str|list): ID or list of IDs of proxy groups to delete.
        
        Returns:
            dict: API response containing the IDs of deleted proxy groups.
        
        Example:
            >>> # Delete a single proxy group
            >>> zapi.proxy_groups.delete(proxygroupid="1")
            >>> 
            >>> # Delete multiple proxy groups
            >>> zapi.proxy_groups.delete(proxygroupid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/proxygroup/delete
        """
        return self._call(f"{self.API_METHOD}.delete", proxygroupid=proxygroupid)

    def get(self, proxy_groupids=None, **filters):
        """
        Retrieve proxy groups according to the given parameters.
        
        Args:
            proxy_groupids (list, optional): Return only proxy groups with the given IDs.
            
        Keyword Args (filters):
            proxyids (str|list, optional): Return only proxy groups that contain the given proxies.
            selectProxies (str|list, optional): Return a proxies property with the proxies that belong to the proxy group. Supports count.
            sortfield (str|list, optional): Sort the result by the given properties. Possible values: proxy_groupid, name.
            countOutput (bool, optional): Return the number of records instead of actual data.
            editable (bool, optional): If true, only return objects that the user has write permissions to.
            excludeSearch (bool, optional): Return results that do not match the criteria given in the search parameter.
            filter (dict, optional): Filter proxy groups by given properties.
            limit (int, optional): Limit the number of records returned.
            output (str|list, optional): Object properties to be returned.
            preservekeys (bool, optional): Use IDs as keys in the resulting array.
            search (dict, optional): Search proxy groups by given properties (case-insensitive).
            searchByAny (bool, optional): Return results that match any of the criteria given in the search parameter instead of all of them.
            searchWildcardsEnabled (bool, optional): Enable the use of "*" as a wildcard character in the search parameter.
            sortorder (str|list, optional): Sort order ("ASC" or "DESC").
            startSearch (bool, optional): Return results that match the criteria given in the search parameter.
        
        Returns:
            dict: API response containing proxy groups matching the criteria.
        
        Example:
            >>> # Get all proxy groups
            >>> proxy_groups = zapi.proxy_groups.get()
            >>> 
            >>> # Get proxy group with proxies
            >>> proxy_group = zapi.proxy_groups.get(proxy_groupids=["1"], selectProxies="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/proxygroup/get
        """
        return self._call(f"{self.API_METHOD}.get", proxy_groupids=proxy_groupids, **filters)
    
    def update(self, proxygroupid, **params):
        """
        Update existing proxy groups.
        
        Args:
            proxygroupid (str): ID of the proxy group to update.
            
        Keyword Args (params):
            name (str, optional): Name of the proxy group.
            failover_delay (int, optional): Failover delay in seconds.
            min_online (int, optional): Minimum number of online proxies in the group.
        
        Returns:
            dict: API response containing the IDs of updated proxy groups.
        
        Example:
            >>> zapi.proxy_groups.update(
            ...     proxygroupid="1",
            ...     name="Updated Proxy Group Name",
            ...     failover_delay=120
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/proxygroup/update
        """
        return self._call(f"{self.API_METHOD}.update", proxygroupid=proxygroupid, **params)