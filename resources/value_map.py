# resources/value_map.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/valuemap

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ValueMapResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "valuemap"
    
    def create(self, **params):
        """
        Create new value mappings.
        
        Keyword Args (params):
            name (str, required): Name of the value mapping.
            mappings (list, required): Value mappings. Each object should contain value, newvalue.
        
        Returns:
            dict: API response containing the IDs of created value mappings.
        
        Example:
            >>> valuemap = zapi.value_maps.create(
            ...     name="Status Mapping",
            ...     mappings=[
            ...         {"value": "0", "newvalue": "OK"},
            ...         {"value": "1", "newvalue": "Error"}
            ...     ]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/valuemap/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, valuemapid):
        """
        Delete value mappings.
        
        Args:
            valuemapid (str|list): ID or list of IDs of value mappings to delete.
        
        Returns:
            dict: API response containing the IDs of deleted value mappings.
        
        Example:
            >>> # Delete a single value mapping
            >>> zapi.value_maps.delete(valuemapid="1")
            >>> 
            >>> # Delete multiple value mappings
            >>> zapi.value_maps.delete(valuemapid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/valuemap/delete
        """
        return self._call(f"{self.API_METHOD}.delete", valuemapid=valuemapid)

    def get(self, valuemapid=None, **filters):
        """
        Retrieve value mappings according to the given parameters.
        
        Args:
            valuemapid (str|list, optional): Return only value mappings with the given IDs.
            
        Keyword Args (filters):
            selectMappings (str|list, optional): Include mappings in the result.
            filter (dict, optional): Filter value mappings by given properties.
            search (dict, optional): Search value mappings by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing value mappings matching the criteria.
        
        Example:
            >>> # Get all value mappings
            >>> valuemaps = zapi.value_maps.get()
            >>> 
            >>> # Get value mapping with mappings
            >>> valuemap = zapi.value_maps.get(valuemapid="1", selectMappings="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/valuemap/get
        """
        return self._call(f"{self.API_METHOD}.get", valuemapid=valuemapid, **filters)
    
    def update(self, valuemapid, **params):
        """
        Update existing value mappings.
        
        Args:
            valuemapid (str): ID of the value mapping to update.
            
        Keyword Args (params):
            name (str, optional): Name of the value mapping.
            mappings (list, optional): Value mappings.
        
        Returns:
            dict: API response containing the IDs of updated value mappings.
        
        Example:
            >>> zapi.value_maps.update(
            ...     valuemapid="1",
            ...     name="Updated Mapping Name",
            ...     mappings=[{"value": "0", "newvalue": "Success"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/valuemap/update
        """
        return self._call(f"{self.API_METHOD}.update", valuemapid=valuemapid, **params)