# resources/graph_prototype.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graphprototype

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class GraphPrototypeResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "graphprototype"

    def create(self, **params):
        """
        Create new graph prototypes.
        
        Keyword Args (params):
            name (str, required): Name of the graph prototype.
            width (int, required): Width of the graph prototype in pixels.
            height (int, required): Height of the graph prototype in pixels.
            graph_items (list, required): Graph item prototypes. Each object should contain itemid, drawtype, sortorder, color, yaxisside, calc_fnc, type.
            gitems (list, required): Alias for graph_items.
            gtype (int, optional): Graph type (0: normal, 1: stacked, 2: pie, 3: exploded).
            show_legend (int, optional): Whether to show the legend (0: hide, 1: show).
            show_3d (int, optional): Whether to show the graph in 3D (0: 2D, 1: 3D).
            percent_left (float, optional): Left percentile line.
            percent_right (float, optional): Right percentile line.
            ymin_type (int, optional): Minimum Y axis value calculation method.
            ymax_type (int, optional): Maximum Y axis value calculation method.
            ymin_itemid (str, optional): Item prototype ID used to calculate minimum Y axis value.
            ymax_itemid (str, optional): Item prototype ID used to calculate maximum Y axis value.
            show_work_period (int, optional): Whether to show working time (0: hide, 1: show).
            show_triggers (int, optional): Whether to show trigger lines (0: hide, 1: show).
            discovery_ruleid (str, required): ID of the LLD rule that the graph prototype belongs to.
            templateid (str, optional): ID of the parent template graph prototype.
        
        Returns:
            dict: API response containing the IDs of created graph prototypes.
        
        Example:
            >>> graph_prototype = zapi.graph_prototypes.create(
            ...     name="CPU utilization for {#CPU.NUMBER}",
            ...     width=900,
            ...     height=200,
            ...     discovery_ruleid="1",
            ...     graph_items=[...]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graphprototype/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, graphprototypeid):
        """
        Delete graph prototypes.
        
        Args:
            graphprototypeid (str|list): ID or list of IDs of graph prototypes to delete.
        
        Returns:
            dict: API response containing the IDs of deleted graph prototypes.
        
        Example:
            >>> # Delete a single graph prototype
            >>> zapi.graph_prototypes.delete(graphprototypeid="1")
            >>> 
            >>> # Delete multiple graph prototypes
            >>> zapi.graph_prototypes.delete(graphprototypeid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graphprototype/delete
        """
        return self._call(f"{self.API_METHOD}.delete", graphprototypeid=graphprototypeid)

    def get(self, graphprototypeid=None, **filters):
        """
        Retrieve graph prototypes according to the given parameters.
        
        Args:
            graphprototypeid (str|list, optional): Return only graph prototypes with the given IDs.
            
        Keyword Args (filters):
            discoveryids (list, optional): Return only graph prototypes that belong to the given LLD rules.
            itemids (list, optional): Return only graph prototypes that contain the given item prototypes.
            selectHosts (str|list, optional): Include hosts in the result.
            selectTemplates (str|list, optional): Include templates in the result.
            selectItems (str|list, optional): Include graph item prototypes in the result.
            selectGraphItems (str|list, optional): Include graph item prototypes in the result (alias for selectItems).
            selectDiscoveryRule (str|list, optional): Include LLD rule in the result.
            filter (dict, optional): Filter graph prototypes by given properties.
            search (dict, optional): Search graph prototypes by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing graph prototypes matching the criteria.
        
        Example:
            >>> # Get all graph prototypes
            >>> graph_prototypes = zapi.graph_prototypes.get()
            >>> 
            >>> # Get graph prototypes for an LLD rule
            >>> graph_prototypes = zapi.graph_prototypes.get(discoveryids=["1"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graphprototype/get
        """
        return self._call(f"{self.API_METHOD}.get", graphprototypeid=graphprototypeid, **filters)

    def update(self, graphprototypeid, **params):
        """
        Update existing graph prototypes.
        
        Args:
            graphprototypeid (str): ID of the graph prototype to update.
            
        Keyword Args (params):
            name (str, optional): Name of the graph prototype.
            width (int, optional): Width of the graph prototype in pixels.
            height (int, optional): Height of the graph prototype in pixels.
            graph_items (list, optional): Graph item prototypes.
            gitems (list, optional): Alias for graph_items.
            gtype (int, optional): Graph type.
            show_legend (int, optional): Whether to show the legend.
            show_3d (int, optional): Whether to show the graph in 3D.
            percent_left (float, optional): Left percentile line.
            percent_right (float, optional): Right percentile line.
            ymin_type (int, optional): Minimum Y axis value calculation method.
            ymax_type (int, optional): Maximum Y axis value calculation method.
            ymin_itemid (str, optional): Item prototype ID for minimum Y axis value.
            ymax_itemid (str, optional): Item prototype ID for maximum Y axis value.
            show_work_period (int, optional): Whether to show working time.
            show_triggers (int, optional): Whether to show trigger lines.
        
        Returns:
            dict: API response containing the IDs of updated graph prototypes.
        
        Example:
            >>> zapi.graph_prototypes.update(
            ...     graphprototypeid="1",
            ...     name="Updated Graph Prototype Name",
            ...     show_legend=1
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graphprototype/update
        """
        return self._call(f"{self.API_METHOD}.update", graphprototypeid=graphprototypeid, **params)