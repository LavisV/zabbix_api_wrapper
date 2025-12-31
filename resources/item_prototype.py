# resources/item_prototype.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/itemprototype

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ItemPrototypeResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "itemprototype"

    def create(self, **params):
        """
        Create new item prototypes.
        
        Keyword Args (params):
            name (str, required): Name of the item prototype.
            key_ (str, required): Item prototype key.
            hostid (str, required): ID of the host that the item prototype belongs to.
            ruleid (str, required): ID of the LLD rule that the item prototype belongs to.
            type (int, required): Type of the item prototype (see Zabbix documentation for type values).
            value_type (int, required): Type of information of the item prototype.
            interfaceid (str, optional): ID of the item prototype's host interface.
            delay (str, optional): Update interval of the item prototype.
            history (str, optional): History storage period.
            trends (str, optional): Trends storage period.
            status (int, optional): Whether the item prototype is enabled (0: enabled, 1: disabled).
            description (str, optional): Description of the item prototype.
            inventory_link (int, optional): ID of the host inventory field.
            posts (str, optional): HTTP agent item query string.
            headers (dict, optional): HTTP agent item HTTP headers.
            parameters (dict, optional): Item-specific parameters.
            tags (list, optional): Item prototype tags.
            preprocessing (list, optional): Preprocessing options.
            master_itemid (str, optional): ID of the master item (for dependent items).
        
        Returns:
            dict: API response containing the IDs of created item prototypes.
        
        Example:
            >>> item_prototype = zapi.item_prototypes.create(
            ...     name="CPU utilization for {#CPU.NUMBER}",
            ...     key_="system.cpu.util[{#CPU.NUMBER}]",
            ...     hostid="10105",
            ...     ruleid="1",
            ...     type=0,
            ...     value_type=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/itemprototype/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, itemprototypeid):
        """
        Delete item prototypes.
        
        Args:
            itemprototypeid (str|list): ID or list of IDs of item prototypes to delete.
        
        Returns:
            dict: API response containing the IDs of deleted item prototypes.
        
        Example:
            >>> # Delete a single item prototype
            >>> zapi.item_prototypes.delete(itemprototypeid="1")
            >>> 
            >>> # Delete multiple item prototypes
            >>> zapi.item_prototypes.delete(itemprototypeid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/itemprototype/delete
        """
        return self._call(f"{self.API_METHOD}.delete", itemprototypeid=itemprototypeid)

    def get(self, itemprototypeid=None, **filters):
        """
        Retrieve item prototypes according to the given parameters.
        
        Args:
            itemprototypeid (str|list, optional): Return only item prototypes with the given IDs.
            
        Keyword Args (filters):
            discoveryids (list, optional): Return only item prototypes that belong to the given LLD rules.
            graphids (list, optional): Return only item prototypes that are used in the given graphs.
            hostids (list, optional): Return only item prototypes that belong to the given hosts.
            inherited (bool, optional): Return only inherited item prototypes.
            monitored (bool, optional): Return only enabled item prototypes that belong to monitored hosts.
            templated (bool, optional): Return only item prototypes that belong to templates.
            selectHosts (str|list, optional): Include hosts in the result.
            selectInterfaces (str|list, optional): Include host interfaces in the result.
            selectTriggers (str|list, optional): Include triggers in the result.
            selectGraphs (str|list, optional): Include graphs in the result.
            selectDiscoveryRule (str|list, optional): Include LLD rule in the result.
            selectPreprocessing (str|list, optional): Include preprocessing options in the result.
            selectTags (str|list, optional): Include tags in the result.
            selectMasterItem (str|bool, optional): Include master item in the result.
            filter (dict, optional): Filter item prototypes by given properties.
            search (dict, optional): Search item prototypes by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing item prototypes matching the criteria.
        
        Example:
            >>> # Get all item prototypes
            >>> prototypes = zapi.item_prototypes.get()
            >>> 
            >>> # Get item prototypes for an LLD rule
            >>> prototypes = zapi.item_prototypes.get(discoveryids=["1"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/itemprototype/get
        """
        return self._call(f"{self.API_METHOD}.get", itemprototypeid=itemprototypeid, **filters)
    
    def update(self, itemprototypeid, **params):
        """
        Update existing item prototypes.
        
        Args:
            itemprototypeid (str): ID of the item prototype to update.
            
        Keyword Args (params):
            name (str, optional): Name of the item prototype.
            key_ (str, optional): Item prototype key.
            hostid (str, optional): ID of the host that the item prototype belongs to.
            ruleid (str, optional): ID of the LLD rule that the item prototype belongs to.
            type (int, optional): Type of the item prototype.
            value_type (int, optional): Type of information of the item prototype.
            interfaceid (str, optional): ID of the item prototype's host interface.
            delay (str, optional): Update interval of the item prototype.
            history (str, optional): History storage period.
            trends (str, optional): Trends storage period.
            status (int, optional): Whether the item prototype is enabled (0: enabled, 1: disabled).
            description (str, optional): Description of the item prototype.
            inventory_link (int, optional): ID of the host inventory field.
            posts (str, optional): HTTP agent item query string.
            headers (dict, optional): HTTP agent item HTTP headers.
            parameters (dict, optional): Item-specific parameters.
            tags (list, optional): Item prototype tags.
            preprocessing (list, optional): Preprocessing options.
            master_itemid (str, optional): ID of the master item.
        
        Returns:
            dict: API response containing the IDs of updated item prototypes.
        
        Example:
            >>> zapi.item_prototypes.update(
            ...     itemprototypeid="1",
            ...     status=1,
            ...     delay="30s"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/itemprototype/update
        """
        return self._call(f"{self.API_METHOD}.update", itemprototypeid=itemprototypeid, **params)