# resources/connector.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ConnectorResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "connector"

    def create(self, **params):
        """
        Create new connectors.
        
        Keyword Args (params):
            name (str, required): Name of the connector.
            data_type (int, required): Data type (0: item values, 1: events, 2: item values and events).
            protocol (int, required): Protocol type (0: HTTP, 1: Kafka, 2: ServiceNow, 3: Jira).
            url (str, optional): URL for HTTP protocol.
            max_records (int, optional): Maximum number of records to send at once.
            max_senders (int, optional): Maximum number of concurrent senders.
            timeout (str, optional): Request timeout.
            http_proxy (str, optional): HTTP proxy connection string.
            verify_peer (int, optional): Verify SSL peer (0: no, 1: yes).
            verify_host (int, optional): Verify SSL host (0: no, 1: yes).
            ssl_cert_file (str, optional): SSL certificate file path.
            ssl_key_file (str, optional): SSL private key file path.
            ssl_key_password (str, optional): SSL private key password.
            token (str, optional): Authentication token.
            authentication_type (int, optional): Authentication type (0: none, 1: basic, 2: token).
            username (str, optional): Username for basic authentication.
            password (str, optional): Password for basic authentication.
            parameters (dict, optional): Protocol-specific parameters.
            tags (list, optional): Connector tags for filtering.
            description (str, optional): Description of the connector.
            status (int, optional): Connector status (0: enabled, 1: disabled).
        
        Returns:
            dict: API response containing the IDs of created connectors.
        
        Example:
            >>> connector = zapi.connectors.create(
            ...     name="External System Connector",
            ...     data_type=0,
            ...     protocol=0,
            ...     url="https://external.example.com/api"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, connectorid):
        """
        Delete connectors.
        
        Args:
            connectorid (str|list): ID or list of IDs of connectors to delete.
        
        Returns:
            dict: API response containing the IDs of deleted connectors.
        
        Example:
            >>> # Delete a single connector
            >>> zapi.connectors.delete(connectorid="1")
            >>> 
            >>> # Delete multiple connectors
            >>> zapi.connectors.delete(connectorid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/delete
        """
        return self._call(f"{self.API_METHOD}.delete", connectorid=connectorid)

    def get(self, connectorid=None, **filters):
        """
        Retrieve connectors according to the given parameters.
        
        Args:
            connectorid (str|list, optional): Return only connectors with the given IDs.
            
        Keyword Args (filters):
            filter (dict, optional): Filter connectors by given properties.
            search (dict, optional): Search connectors by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing connectors matching the criteria.
        
        Example:
            >>> # Get all connectors
            >>> connectors = zapi.connectors.get()
            >>> 
            >>> # Get connector by ID
            >>> connector = zapi.connectors.get(connectorid="1")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/get
        """
        return self._call(f"{self.API_METHOD}.get", connectorid=connectorid, **filters)
    
    def update(self, connectorid, **params):
        """
        Update existing connectors.
        
        Args:
            connectorid (str): ID of the connector to update.
            
        Keyword Args (params):
            name (str, optional): Name of the connector.
            data_type (int, optional): Data type (0: item values, 1: events, 2: item values and events).
            protocol (int, optional): Protocol type.
            url (str, optional): URL for HTTP protocol.
            max_records (int, optional): Maximum number of records to send at once.
            max_senders (int, optional): Maximum number of concurrent senders.
            timeout (str, optional): Request timeout.
            http_proxy (str, optional): HTTP proxy connection string.
            verify_peer (int, optional): Verify SSL peer (0: no, 1: yes).
            verify_host (int, optional): Verify SSL host (0: no, 1: yes).
            ssl_cert_file (str, optional): SSL certificate file path.
            ssl_key_file (str, optional): SSL private key file path.
            ssl_key_password (str, optional): SSL private key password.
            token (str, optional): Authentication token.
            authentication_type (int, optional): Authentication type.
            username (str, optional): Username for basic authentication.
            password (str, optional): Password for basic authentication.
            parameters (dict, optional): Protocol-specific parameters.
            tags (list, optional): Connector tags for filtering.
            description (str, optional): Description of the connector.
            status (int, optional): Connector status (0: enabled, 1: disabled).
        
        Returns:
            dict: API response containing the IDs of updated connectors.
        
        Example:
            >>> zapi.connectors.update(
            ...     connectorid="1",
            ...     name="Updated Connector Name",
            ...     status=1
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/update
        """
        return self._call(f"{self.API_METHOD}.update", connectorid=connectorid, **params)