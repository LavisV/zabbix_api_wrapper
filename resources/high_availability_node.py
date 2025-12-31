# resources/high_availability_node.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hanode

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HighAvailabilityNodeResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "hanode"

    def create(self, **params):
        """
        Create new high availability nodes.
        
        Keyword Args (params):
            name (str, required): Name of the HA node.
            address (str, required): Address of the HA node.
            port (int, required): Port of the HA node.
            internal_address (str, optional): Internal address of the HA node.
            internal_port (int, optional): Internal port of the HA node.
            nodeid (int, optional): Node ID.
        
        Returns:
            dict: API response containing the IDs of created HA nodes.
        
        Example:
            >>> ha_node = zapi.high_availability_nodes.create(
            ...     name="Node 1",
            ...     address="192.168.1.10",
            ...     port=10051
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hanode/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, highavailabilitynodeid):
        """
        Delete high availability nodes.
        
        Args:
            highavailabilitynodeid (str|list): ID or list of IDs of HA nodes to delete.
        
        Returns:
            dict: API response containing the IDs of deleted HA nodes.
        
        Example:
            >>> # Delete a single HA node
            >>> zapi.high_availability_nodes.delete(highavailabilitynodeid="1")
            >>> 
            >>> # Delete multiple HA nodes
            >>> zapi.high_availability_nodes.delete(highavailabilitynodeid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hanode/delete
        """
        return self._call(f"{self.API_METHOD}.delete", highavailabilitynodeid=highavailabilitynodeid)

    def get(self, highavailabilitynodeid=None, **filters):
        """
        Retrieve high availability nodes according to the given parameters.
        
        Args:
            highavailabilitynodeid (str|list, optional): Return only HA nodes with the given IDs.
            
        Keyword Args (filters):
            filter (dict, optional): Filter HA nodes by given properties.
            search (dict, optional): Search HA nodes by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing HA nodes matching the criteria.
        
        Example:
            >>> # Get all HA nodes
            >>> ha_nodes = zapi.high_availability_nodes.get()
            >>> 
            >>> # Get HA node by ID
            >>> ha_node = zapi.high_availability_nodes.get(highavailabilitynodeid="1")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hanode/get
        """
        return self._call(f"{self.API_METHOD}.get", highavailabilitynodeid=highavailabilitynodeid, **filters)