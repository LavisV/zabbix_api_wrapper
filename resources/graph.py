# resources/graph.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class GraphResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "graph"

    def create(self, **params):
        """
        Create new graphs.
        
        Keyword Args (params):
            name (str, required): Name of the graph.
            width (int, required): Width of the graph in pixels.
            height (int, required): Height of the graph in pixels.
            graph_items (list, required): Graph items. Each object should contain itemid, drawtype, sortorder, color, yaxisside, calc_fnc, type.
            gitems (list, required): Alias for graph_items.
            gtype (int, optional): Graph type (0: normal, 1: stacked, 2: pie, 3: exploded).
            show_legend (int, optional): Whether to show the legend (0: hide, 1: show).
            show_3d (int, optional): Whether to show the graph in 3D (0: 2D, 1: 3D).
            percent_left (float, optional): Left percentile line.
            percent_right (float, optional): Right percentile line.
            ymin_type (int, optional): Minimum Y axis value calculation method.
            ymax_type (int, optional): Maximum Y axis value calculation method.
            ymin_itemid (str, optional): Item ID used to calculate minimum Y axis value.
            ymax_itemid (str, optional): Item ID used to calculate maximum Y axis value.
            show_work_period (int, optional): Whether to show working time (0: hide, 1: show).
            show_triggers (int, optional): Whether to show trigger lines (0: hide, 1: show).
            templateid (str, optional): ID of the parent template graph.
            flags (int, optional): Origin of the graph (0: plain graph, 4: discovered graph).
        
        Returns:
            dict: API response containing the IDs of created graphs.
        
        Example:
            >>> graph = zapi.graphs.create(
            ...     name="CPU Utilization Graph",
            ...     width=900,
            ...     height=200,
            ...     graph_items=[{
            ...         "itemid": "12345",
            ...         "drawtype": 0,
            ...         "sortorder": 0,
            ...         "color": "00AA00"
            ...     }]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, graphid):
        """
        Delete graphs.
        
        Args:
            graphid (str|list): ID or list of IDs of graphs to delete.
        
        Returns:
            dict: API response containing the IDs of deleted graphs.
        
        Example:
            >>> # Delete a single graph
            >>> zapi.graphs.delete(graphid="1")
            >>> 
            >>> # Delete multiple graphs
            >>> zapi.graphs.delete(graphid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph/delete
        """
        return self._call(f"{self.API_METHOD}.delete", graphid=graphid)

    def get(self, graphid=None, **filters):
        """
        Retrieve graphs according to the given parameters.
        
        Args:
            graphid (str|list, optional): Return only graphs with the given IDs.
            
        Keyword Args (filters):
            groupids (list, optional): Return only graphs that belong to the given host groups.
            templateids (list, optional): Return only graphs that belong to the given templates.
            hostids (list, optional): Return only graphs that belong to the given hosts.
            itemids (list, optional): Return only graphs that contain the given items.
            graphids (list, optional): Return only graphs with the given IDs (alias for graphid).
            expandName (bool, optional): Expand graph name with item name.
            selectHostGroups (str|list, optional): Include host groups in the result.
            selectTemplates (str|list, optional): Include templates in the result.
            selectHosts (str|list, optional): Include hosts in the result.
            selectItems (str|list, optional): Include graph items in the result.
            selectGraphItems (str|list, optional): Include graph items in the result.
            selectGroups (str|list, optional): Include host groups in the result (alias for selectHostGroups).
            filter (dict, optional): Filter graphs by given properties.
            search (dict, optional): Search graphs by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing graphs matching the criteria.
        
        Example:
            >>> # Get all graphs
            >>> graphs = zapi.graphs.get()
            >>> 
            >>> # Get graphs for a host
            >>> graphs = zapi.graphs.get(hostids=["10105"])
            >>> 
            >>> # Get graphs with items
            >>> graphs = zapi.graphs.get(selectItems="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph/get
        """
        return self._call(f"{self.API_METHOD}.get", graphid=graphid, **filters)
    
    def update(self, graphid, **params):
        """
        Update existing graphs.
        
        Args:
            graphid (str): ID of the graph to update.
            
        Keyword Args (params):
            name (str, optional): Name of the graph.
            width (int, optional): Width of the graph in pixels.
            height (int, optional): Height of the graph in pixels.
            graph_items (list, optional): Graph items.
            gitems (list, optional): Alias for graph_items.
            gtype (int, optional): Graph type (0: normal, 1: stacked, 2: pie, 3: exploded).
            show_legend (int, optional): Whether to show the legend (0: hide, 1: show).
            show_3d (int, optional): Whether to show the graph in 3D (0: 2D, 1: 3D).
            percent_left (float, optional): Left percentile line.
            percent_right (float, optional): Right percentile line.
            ymin_type (int, optional): Minimum Y axis value calculation method.
            ymax_type (int, optional): Maximum Y axis value calculation method.
            ymin_itemid (str, optional): Item ID used to calculate minimum Y axis value.
            ymax_itemid (str, optional): Item ID used to calculate maximum Y axis value.
            show_work_period (int, optional): Whether to show working time (0: hide, 1: show).
            show_triggers (int, optional): Whether to show trigger lines (0: hide, 1: show).
        
        Returns:
            dict: API response containing the IDs of updated graphs.
        
        Example:
            >>> zapi.graphs.update(
            ...     graphid="1",
            ...     name="Updated Graph Name",
            ...     show_legend=1
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph/update
        """
        return self._call(f"{self.API_METHOD}.update", graphid=graphid, **params)