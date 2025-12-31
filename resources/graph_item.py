# resources/graph_item.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graphitem

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class GraphItemResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "graphitem"

    def get(self, **filters):
        """
        Retrieve graph items according to the given parameters.
        
        Keyword Args (filters):
            graphids (list, optional): Return only graph items that belong to the given graphs.
            itemids (list, optional): Return only graph items that use the given items.
            type (int, optional): Return only graph items of the given type (0: simple, 1: sum).
            filter (dict, optional): Filter graph items by given properties.
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing graph items matching the criteria.
        
        Example:
            >>> # Get all graph items
            >>> graph_items = zapi.graph_items.get()
            >>> 
            >>> # Get graph items for a graph
            >>> graph_items = zapi.graph_items.get(graphids=["1"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graphitem/get
        """
        return self._call(f"{self.API_METHOD}.get", **filters)