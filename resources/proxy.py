# resources/proxy.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/proxy

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ProxyResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "proxy"

    def create(self, **params):
        """
        Create new proxies.
        
        Keyword Args (params):
            host (str, required): Technical name of the proxy.
            status (int, required): Status of the proxy (5: active, 6: passive).
            interfaces (list, optional): Proxy interfaces (required for active proxies).
            description (str, optional): Description of the proxy.
            tls_connect (int, optional): Connections to proxy.
            tls_accept (int, optional): Connections from proxy.
            tls_issuer (str, optional): Certificate issuer.
            tls_subject (str, optional): Certificate subject.
            tls_psk_identity (str, optional): PSK identity.
            tls_psk (str, optional): PSK value.
            proxy_address (str, optional): Proxy address (required for passive proxies).
            proxyid (str, optional): Proxy ID (for active proxies).
        
        Returns:
            dict: API response containing the IDs of created proxies.
        
        Example:
            >>> proxy = zapi.proxies.create(
            ...     host="proxy1",
            ...     status=5
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/proxy/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, proxyid):
        """
        Delete proxies.
        
        Args:
            proxyid (str|list): ID or list of IDs of proxies to delete.
        
        Returns:
            dict: API response containing the IDs of deleted proxies.
        
        Example:
            >>> # Delete a single proxy
            >>> zapi.proxies.delete(proxyid="1")
            >>> 
            >>> # Delete multiple proxies
            >>> zapi.proxies.delete(proxyid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/proxy/delete
        """
        return self._call(f"{self.API_METHOD}.delete", proxyid=proxyid)

    def get(self, proxyids=None, **filters):
        """
        Retrieve proxies according to the given parameters.
        
        Args:
            proxyids (list, optional): Return only proxies with the given IDs.
            
        Keyword Args (filters):
            proxy_groupids (str|list, optional): Return only proxies that belong to the given proxy groups.
            selectAssignedHosts (str|list, optional): Return an assignedHosts property with the hosts assigned to the proxy. Supports count.
            selectHosts (str|list, optional): Return a hosts property with the hosts monitored by the proxy. Supports count.
            selectProxyGroup (str|list, optional): Return a proxyGroup property with the proxy group object.
            sortfield (str|list, optional): Sort the result by the given properties. Possible values: proxyid, name, operating_mode.
            countOutput (bool, optional): Return the number of records instead of actual data.
            editable (bool, optional): If true, only return objects that the user has write permissions to.
            excludeSearch (bool, optional): Return results that do not match the criteria given in the search parameter.
            filter (dict, optional): Filter proxies by given properties.
            limit (int, optional): Limit the number of records returned.
            output (str|list, optional): Object properties to be returned.
            preservekeys (bool, optional): Use IDs as keys in the resulting array.
            search (dict, optional): Search proxies by given properties (case-insensitive).
            searchByAny (bool, optional): Return results that match any of the criteria given in the search parameter instead of all of them.
            searchWildcardsEnabled (bool, optional): Enable the use of "*" as a wildcard character in the search parameter.
            sortorder (str|list, optional): Sort order ("ASC" or "DESC").
            startSearch (bool, optional): Return results that match the criteria given in the search parameter.
        
        Returns:
            dict: API response containing proxies matching the criteria.
        
        Example:
            >>> # Get all proxies
            >>> proxies = zapi.proxies.get()
            >>> 
            >>> # Get proxies with hosts
            >>> proxies = zapi.proxies.get(selectHosts="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/proxy/get
        """
        return self._call(f"{self.API_METHOD}.get", proxyids=proxyids, **filters)
    
    def update(self, proxyid, **params):
        """
        Update existing proxies.
        
        Args:
            proxyid (str): ID of the proxy to update.
            
        Keyword Args (params):
            host (str, optional): Technical name of the proxy.
            status (int, optional): Status of the proxy (5: active, 6: passive).
            interfaces (list, optional): Proxy interfaces.
            description (str, optional): Description of the proxy.
            tls_connect (int, optional): Connections to proxy.
            tls_accept (int, optional): Connections from proxy.
            tls_issuer (str, optional): Certificate issuer.
            tls_subject (str, optional): Certificate subject.
            tls_psk_identity (str, optional): PSK identity.
            tls_psk (str, optional): PSK value.
            proxy_address (str, optional): Proxy address (for passive proxies).
        
        Returns:
            dict: API response containing the IDs of updated proxies.
        
        Example:
            >>> zapi.proxies.update(
            ...     proxyid="1",
            ...     description="Updated Proxy"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/proxy/update
        """
        return self._call(f"{self.API_METHOD}.update", proxyid=proxyid, **params)