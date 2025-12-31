# resources/item.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/item

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ItemResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)    

    API_METHOD = "item"

    def create(self, **params):
        """
        Create new items.
        
        Keyword Args (params):
            name (str, required): Name of the item.
            key_ (str, required): Item key.
            hostid (str, required): ID of the host that the item belongs to.
            type (int, required): Type of the item (see Zabbix documentation for type values).
            value_type (int, required): Type of information of the item.
            interfaceid (str, optional): ID of the item's host interface.
            delay (str, optional): Update interval of the item.
            history (str, optional): History storage period.
            trends (str, optional): Trends storage period.
            status (int, optional): Whether the item is enabled (0: enabled, 1: disabled).
            description (str, optional): Description of the item.
            inventory_link (int, optional): ID of the host inventory field.
            posts (str, optional): HTTP agent item query string.
            headers (dict, optional): HTTP agent item HTTP headers.
            parameters (dict, optional): Item-specific parameters.
            tags (list, optional): Item tags.
            preprocessing (list, optional): Preprocessing options.
        
        Returns:
            dict: API response containing the IDs of created items.
        
        Example:
            >>> item = zapi.items.create(
            ...     name="CPU utilization",
            ...     key_="system.cpu.util",
            ...     hostid="10105",
            ...     type=0,
            ...     value_type=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/item/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, itemid):
        """
        Delete items.
        
        Args:
            itemid (str|list): ID or list of IDs of items to delete.
        
        Returns:
            dict: API response containing the IDs of deleted items.
        
        Example:
            >>> # Delete a single item
            >>> zapi.items.delete(itemid="12345")
            >>> 
            >>> # Delete multiple items
            >>> zapi.items.delete(itemid=["12345", "12346"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/item/delete
        """
        return self._call(f"{self.API_METHOD}.delete", itemid=itemid)

    def get(self, itemid=None, **filters):
        """
        Retrieve items according to the given parameters.
        
        Args:
            itemid (str|list, optional): Return only items with the given IDs.
            
        Keyword Args (filters):
            groupids (list, optional): Return only items that belong to the given host groups.
            templateids (list, optional): Return only items that belong to the given templates.
            hostids (list, optional): Return only items that belong to the given hosts.
            proxyids (list, optional): Return only items that are monitored by the given proxies.
            interfaceids (list, optional): Return only items that use the given host interfaces.
            graphids (list, optional): Return only items used in the given graphs.
            triggerids (list, optional): Return only items used in the given triggers.
            applicationids (list, optional): Return only items that belong to the given applications.
            webitems (bool, optional): Return only web items.
            inherited (bool, optional): Return only inherited items.
            templated (bool, optional): Return only items that belong to templates.
            monitored (bool, optional): Return only enabled items that belong to monitored hosts.
            group (str, optional): Return only items that belong to a host group with the given name.
            host (str, optional): Return only items that belong to a host with the given name.
            application (str, optional): Return only items that belong to an application with the given name.
            with_triggers (bool, optional): Return only items that have triggers.
            selectHosts (str|list, optional): Include hosts in the result.
            selectInterfaces (str|list, optional): Include host interfaces in the result.
            selectTriggers (str|list, optional): Include triggers in the result.
            selectGraphs (str|list, optional): Include graphs in the result.
            selectApplications (str|list, optional): Include applications in the result.
            selectDiscoveryRule (str|list, optional): Include LLD rule in the result.
            selectItemDiscovery (str|list, optional): Include item discovery in the result.
            selectPreprocessing (str|list, optional): Include preprocessing options in the result.
            selectTags (str|list, optional): Include tags in the result.
            selectValueMap (str|bool, optional): Include value mapping in the result.
            filter (dict, optional): Filter items by given properties.
            search (dict, optional): Search items by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing items matching the criteria.
        
        Example:
            >>> # Get all items for a host
            >>> items = zapi.items.get(hostids=["10105"])
            >>> 
            >>> # Get items with triggers
            >>> items = zapi.items.get(with_triggers=True)
            >>> 
            >>> # Get items by application
            >>> items = zapi.items.get(applicationids=["1"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/item/get
        """
        return self._call(f"{self.API_METHOD}.get", itemid=itemid, **filters)
    
    def update(self, itemid, **params):
        """
        Update existing items.
        
        Args:
            itemid (str): ID of the item to update.
            
        Keyword Args (params):
            name (str, optional): Name of the item.
            key_ (str, optional): Item key.
            hostid (str, optional): ID of the host that the item belongs to.
            type (int, optional): Type of the item.
            value_type (int, optional): Type of information of the item.
            interfaceid (str, optional): ID of the item's host interface.
            delay (str, optional): Update interval of the item.
            history (str, optional): History storage period.
            trends (str, optional): Trends storage period.
            status (int, optional): Whether the item is enabled (0: enabled, 1: disabled).
            description (str, optional): Description of the item.
            inventory_link (int, optional): ID of the host inventory field.
            posts (str, optional): HTTP agent item query string.
            headers (dict, optional): HTTP agent item HTTP headers.
            parameters (dict, optional): Item-specific parameters.
            tags (list, optional): Item tags.
            preprocessing (list, optional): Preprocessing options.
        
        Returns:
            dict: API response containing the IDs of updated items.
        
        Example:
            >>> zapi.items.update(
            ...     itemid="12345",
            ...     status=1,
            ...     delay="30s"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/item/update
        """
        return self._call(f"{self.API_METHOD}.update", itemid=itemid, **params)