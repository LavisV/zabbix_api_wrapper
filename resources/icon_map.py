# resources/icon_map.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/iconmap
try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class IconMapResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "iconmap"

    def create(self, **params):
        """
        Create new icon maps.
        
        Keyword Args (params):
            name (str, required): Name of the icon map.
            default_iconid (str, required): ID of the default icon.
            mappings (list, required): Icon map mappings. Each object should contain iconid, inventory_link, expression, expression_type.
        
        Returns:
            dict: API response containing the IDs of created icon maps.
        
        Example:
            >>> icon_map = zapi.icon_maps.create(
            ...     name="Host Type Icons",
            ...     default_iconid="1",
            ...     mappings=[{
            ...         "iconid": "2",
            ...         "inventory_link": 1,
            ...         "expression": "Linux",
            ...         "expression_type": 0
            ...     }]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/iconmap/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, iconmapid):
        """
        Delete icon maps.
        
        Args:
            iconmapid (str|list): ID or list of IDs of icon maps to delete.
        
        Returns:
            dict: API response containing the IDs of deleted icon maps.
        
        Example:
            >>> # Delete a single icon map
            >>> zapi.icon_maps.delete(iconmapid="1")
            >>> 
            >>> # Delete multiple icon maps
            >>> zapi.icon_maps.delete(iconmapid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/iconmap/delete
        """
        return self._call(f"{self.API_METHOD}.delete", iconmapid=iconmapid)

    def get(self, iconmapid=None, **filters):
        """
        Retrieve icon maps according to the given parameters.
        
        Args:
            iconmapid (str|list, optional): Return only icon maps with the given IDs.
            
        Keyword Args (filters):
            selectMappings (str|list, optional): Include mappings in the result.
            filter (dict, optional): Filter icon maps by given properties.
            search (dict, optional): Search icon maps by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing icon maps matching the criteria.
        
        Example:
            >>> # Get all icon maps
            >>> icon_maps = zapi.icon_maps.get()
            >>> 
            >>> # Get icon map with mappings
            >>> icon_map = zapi.icon_maps.get(iconmapid="1", selectMappings="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/iconmap/get
        """
        return self._call(f"{self.API_METHOD}.get", iconmapid=iconmapid, **filters)
    
    def update(self, iconmapid, **params):
        """
        Update existing icon maps.
        
        Args:
            iconmapid (str): ID of the icon map to update.
            
        Keyword Args (params):
            name (str, optional): Name of the icon map.
            default_iconid (str, optional): ID of the default icon.
            mappings (list, optional): Icon map mappings.
        
        Returns:
            dict: API response containing the IDs of updated icon maps.
        
        Example:
            >>> zapi.icon_maps.update(
            ...     iconmapid="1",
            ...     name="Updated Icon Map Name",
            ...     default_iconid="3"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/iconmap/update
        """
        return self._call(f"{self.API_METHOD}.update", iconmapid=iconmapid, **params)