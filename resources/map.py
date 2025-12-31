# resources/map.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/map

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class MapResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "map"

    def create(self, **params):
        """
        Create new network maps.
        
        Keyword Args (params):
            name (str, required): Name of the map.
            width (int, required): Width of the map in pixels.
            height (int, required): Height of the map in pixels.
            backgroundid (str, optional): ID of the image used as map background.
            label_type (int, optional): Map label type (0: label, 1: IP address, 2: name, 3: status, 4: nothing, 5: custom).
            label_location (int, optional): Map label location (0: bottom, 1: left, 2: right, 3: top).
            highlight (int, optional): Whether to highlight map elements (0: no, 1: yes).
            expandproblem (int, optional): Whether to expand single problem (0: no, 1: yes).
            markelements (int, optional): Whether to mark elements on trigger status change (0: no, 1: yes).
            show_unack (int, optional): Whether to show unacknowledged problems (0: no, 1: yes).
            grid_size (int, optional): Grid size in pixels.
            grid_show (int, optional): Whether to show grid (0: no, 1: yes).
            grid_align (int, optional): Whether to align to grid (0: no, 1: yes).
            label_format (int, optional): Map label format (0: image, 1: text).
            label_type_host (int, optional): Host label type.
            label_type_hostgroup (int, optional): Host group label type.
            label_type_trigger (int, optional): Trigger label type.
            label_type_map (int, optional): Map label type.
            label_type_image (int, optional): Image label type.
            label_string_host (str, optional): Host label string.
            label_string_hostgroup (str, optional): Host group label string.
            label_string_trigger (str, optional): Trigger label string.
            label_string_map (str, optional): Map label string.
            label_string_image (str, optional): Image label string.
            expand_macros (int, optional): Whether to expand macros in labels (0: no, 1: yes).
            severity_min (int, optional): Minimum severity to display (0-5).
            iconmapid (str, optional): ID of the icon map.
            urls (list, optional): Map URLs.
            selements (list, optional): Map elements.
            links (list, optional): Map links.
            userid (str, optional): ID of the user who owns the map.
            private (int, optional): Map sharing (0: public, 1: private).
            show_suppressed (int, optional): Whether to show suppressed problems (0: no, 1: yes).
        
        Returns:
            dict: API response containing the IDs of created maps.
        
        Example:
            >>> map_obj = zapi.maps.create(
            ...     name="Network Map",
            ...     width=800,
            ...     height=600
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/map/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, mapid):
        """
        Delete network maps.
        
        Args:
            mapid (str|list): ID or list of IDs of maps to delete.
        
        Returns:
            dict: API response containing the IDs of deleted maps.
        
        Example:
            >>> # Delete a single map
            >>> zapi.maps.delete(mapid="1")
            >>> 
            >>> # Delete multiple maps
            >>> zapi.maps.delete(mapid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/map/delete
        """
        return self._call(f"{self.API_METHOD}.delete", mapid=mapid)

    def get(self, mapid=None, **filters):
        """
        Retrieve network maps according to the given parameters.
        
        Args:
            mapid (str|list, optional): Return only maps with the given IDs.
            
        Keyword Args (filters):
            sysmapids (list, optional): Return only maps with the given IDs (alias for mapid).
            selectSelements (str|list, optional): Include map elements in the result.
            selectLinks (str|list, optional): Include map links in the result.
            selectUrls (str|list, optional): Include URLs in the result.
            selectUsers (str|list, optional): Include users in the result.
            selectUserGroups (str|list, optional): Include user groups in the result.
            selectIconMap (str|bool, optional): Include icon map in the result.
            selectIcon (str|bool, optional): Include icon in the result.
            filter (dict, optional): Filter maps by given properties.
            search (dict, optional): Search maps by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing maps matching the criteria.
        
        Example:
            >>> # Get all maps
            >>> maps = zapi.maps.get()
            >>> 
            >>> # Get map with elements and links
            >>> map_obj = zapi.maps.get(mapid="1", selectSelements="extend", selectLinks="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/map/get
        """
        return self._call(f"{self.API_METHOD}.get", mapid=mapid, **filters)
    
    def update(self, mapid, **params):
        """
        Update existing network maps.
        
        Args:
            mapid (str): ID of the map to update.
            
        Keyword Args (params):
            name (str, optional): Name of the map.
            width (int, optional): Width of the map in pixels.
            height (int, optional): Height of the map in pixels.
            backgroundid (str, optional): ID of the image used as map background.
            label_type (int, optional): Map label type.
            label_location (int, optional): Map label location.
            highlight (int, optional): Whether to highlight map elements.
            expandproblem (int, optional): Whether to expand single problem.
            markelements (int, optional): Whether to mark elements on trigger status change.
            show_unack (int, optional): Whether to show unacknowledged problems.
            grid_size (int, optional): Grid size in pixels.
            grid_show (int, optional): Whether to show grid.
            grid_align (int, optional): Whether to align to grid.
            label_format (int, optional): Map label format.
            label_type_host (int, optional): Host label type.
            label_type_hostgroup (int, optional): Host group label type.
            label_type_trigger (int, optional): Trigger label type.
            label_type_map (int, optional): Map label type.
            label_type_image (int, optional): Image label type.
            label_string_host (str, optional): Host label string.
            label_string_hostgroup (str, optional): Host group label string.
            label_string_trigger (str, optional): Trigger label string.
            label_string_map (str, optional): Map label string.
            label_string_image (str, optional): Image label string.
            expand_macros (int, optional): Whether to expand macros in labels.
            severity_min (int, optional): Minimum severity to display.
            iconmapid (str, optional): ID of the icon map.
            urls (list, optional): Map URLs.
            selements (list, optional): Map elements.
            links (list, optional): Map links.
            userid (str, optional): ID of the user who owns the map.
            private (int, optional): Map sharing (0: public, 1: private).
            show_suppressed (int, optional): Whether to show suppressed problems.
        
        Returns:
            dict: API response containing the IDs of updated maps.
        
        Example:
            >>> zapi.maps.update(
            ...     mapid="1",
            ...     name="Updated Map Name",
            ...     width=1000,
            ...     height=800
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/map/update
        """
        return self._call(f"{self.API_METHOD}.update", mapid=mapid, **params)