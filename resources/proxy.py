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

    def get(self, proxyid=None, **filters):
        """
        Retrieve proxies according to the given parameters.
        
        Args:
            proxyid (str|list, optional): Return only proxies with the given IDs.
            
        Keyword Args (filters):
            selectHosts (str|list, optional): Include hosts monitored by the proxy in the result.
            selectInterface (str|bool, optional): Include proxy interface in the result.
            filter (dict, optional): Filter proxies by given properties.
            search (dict, optional): Search proxies by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
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
        return self._call(f"{self.API_METHOD}.get", proxyid=proxyid, **filters)
    
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