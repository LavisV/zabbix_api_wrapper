# resources/web_scenario.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/httptest


try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class WebScenarioResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "httptest"
    
    def create(self, **params):
        """
        Create new web scenarios.
        
        Keyword Args (params):
            name (str, required): Name of the web scenario.
            hostid (str, required): ID of the host that the web scenario belongs to.
            steps (list, required): Web scenario steps. Each object should contain name, url, required, status_codes, variables, headers, follow_redirects, retrieve_mode, timeout.
            delay (str, optional): Update interval of the web scenario.
            status (int, optional): Whether the web scenario is enabled (0: enabled, 1: disabled).
            variables (list, optional): Web scenario variables.
            agent (str, optional): HTTP agent user agent string.
            authentication (int, optional): Authentication method (0: none, 1: basic, 2: NTLM, 3: Kerberos).
            http_user (str, optional): HTTP user for basic authentication.
            http_password (str, optional): HTTP password for basic authentication.
            http_proxy (str, optional): HTTP proxy connection string.
            retries (int, optional): Number of retry attempts.
            ssl_cert_file (str, optional): SSL certificate file path.
            ssl_key_file (str, optional): SSL private key file path.
            ssl_key_password (str, optional): SSL private key password.
            verify_peer (int, optional): Verify SSL peer (0: no, 1: yes).
            verify_host (int, optional): Verify SSL host (0: no, 1: yes).
            headers (dict, optional): HTTP headers.
            tags (list, optional): Web scenario tags.
        
        Returns:
            dict: API response containing the IDs of created web scenarios.
        
        Example:
            >>> scenario = zapi.web_scenarios.create(
            ...     name="Website Check",
            ...     hostid="10105",
            ...     steps=[{
            ...         "name": "Homepage",
            ...         "url": "https://example.com",
            ...         "required": "",
            ...         "status_codes": 200
            ...     }]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/httptest/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, httptestid):
        """
        Delete web scenarios.
        
        Args:
            httptestid (str|list): ID or list of IDs of web scenarios to delete.
        
        Returns:
            dict: API response containing the IDs of deleted web scenarios.
        
        Example:
            >>> # Delete a single web scenario
            >>> zapi.web_scenarios.delete(httptestid="1")
            >>> 
            >>> # Delete multiple web scenarios
            >>> zapi.web_scenarios.delete(httptestid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/httptest/delete
        """
        return self._call(f"{self.API_METHOD}.delete", httptestid=httptestid)

    def get(self, httptestid=None, **filters):
        """
        Retrieve web scenarios according to the given parameters.
        
        Args:
            httptestid (str|list, optional): Return only web scenarios with the given IDs.
            
        Keyword Args (filters):
            groupids (list, optional): Return only web scenarios that belong to the given host groups.
            hostids (list, optional): Return only web scenarios that belong to the given hosts.
            selectSteps (str|list, optional): Include web scenario steps in the result.
            selectTags (str|list, optional): Include tags in the result.
            filter (dict, optional): Filter web scenarios by given properties.
            search (dict, optional): Search web scenarios by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing web scenarios matching the criteria.
        
        Example:
            >>> # Get all web scenarios
            >>> scenarios = zapi.web_scenarios.get()
            >>> 
            >>> # Get web scenarios for a host
            >>> scenarios = zapi.web_scenarios.get(hostids=["10105"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/httptest/get
        """
        return self._call(f"{self.API_METHOD}.get", httptestid=httptestid, **filters)
    
    def update(self, httptestid, **params):
        """
        Update existing web scenarios.
        
        Args:
            httptestid (str): ID of the web scenario to update.
            
        Keyword Args (params):
            name (str, optional): Name of the web scenario.
            hostid (str, optional): ID of the host that the web scenario belongs to.
            steps (list, optional): Web scenario steps.
            delay (str, optional): Update interval of the web scenario.
            status (int, optional): Whether the web scenario is enabled (0: enabled, 1: disabled).
            variables (list, optional): Web scenario variables.
            agent (str, optional): HTTP agent user agent string.
            authentication (int, optional): Authentication method.
            http_user (str, optional): HTTP user for basic authentication.
            http_password (str, optional): HTTP password for basic authentication.
            http_proxy (str, optional): HTTP proxy connection string.
            retries (int, optional): Number of retry attempts.
            ssl_cert_file (str, optional): SSL certificate file path.
            ssl_key_file (str, optional): SSL private key file path.
            ssl_key_password (str, optional): SSL private key password.
            verify_peer (int, optional): Verify SSL peer (0: no, 1: yes).
            verify_host (int, optional): Verify SSL host (0: no, 1: yes).
            headers (dict, optional): HTTP headers.
            tags (list, optional): Web scenario tags.
        
        Returns:
            dict: API response containing the IDs of updated web scenarios.
        
        Example:
            >>> zapi.web_scenarios.update(
            ...     httptestid="1",
            ...     name="Updated Scenario Name",
            ...     status=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/httptest/update
        """
        return self._call(f"{self.API_METHOD}.update", httptestid=httptestid, **params)