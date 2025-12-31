# resources/script.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ScriptResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "script"

    def create(self, **params):
        """
        Create new scripts.
        
        Keyword Args (params):
            name (str, required): Name of the script.
            command (str, required): Command to run.
            host_access (int, required): Host permissions (0: no access, 2: read, 3: write).
            usrgrpid (str, optional): User group ID that will be used to run the script.
            groupid (str, optional): Host group ID where the script can be executed.
            description (str, optional): Description of the script.
            confirmation (str, optional): Confirmation text.
            type (int, optional): Script type (0: script, 1: IPMI, 2: SSH, 3: Telnet, 4: Global script, 5: Webhook).
            execute_on (int, optional): Where to run the script (0: Zabbix agent, 1: Zabbix server, 2: Zabbix server (proxy)).
            timeout (str, optional): Script execution timeout.
            scope (int, optional): Script scope (0: action, 1: host, 2: event).
            menu_path (str, optional): Menu path for the script.
            parameters (list, optional): Script parameters.
        
        Returns:
            dict: API response containing the IDs of created scripts.
        
        Example:
            >>> script = zapi.scripts.create(
            ...     name="Test Script",
            ...     command="echo 'Hello World'",
            ...     host_access=2
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, scriptid):
        """
        Delete scripts.
        
        Args:
            scriptid (str|list): ID or list of IDs of scripts to delete.
        
        Returns:
            dict: API response containing the IDs of deleted scripts.
        
        Example:
            >>> # Delete a single script
            >>> zapi.scripts.delete(scriptid="1")
            >>> 
            >>> # Delete multiple scripts
            >>> zapi.scripts.delete(scriptid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/delete
        """
        return self._call(f"{self.API_METHOD}.delete", scriptid=scriptid)

    def execute(self, scriptid, **params):
        """
        Execute a script.
        
        Args:
            scriptid (str): ID of the script to execute.
            
        Keyword Args (params):
            hostid (str, optional): ID of the host to execute the script on.
            eventid (str, optional): ID of the event (required for event scope scripts).
        
        Returns:
            dict: API response containing script execution results.
        
        Example:
            >>> result = zapi.scripts.execute(scriptid="1", hostid="10105")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/execute
        """
        return self._call(f"{self.API_METHOD}.execute", scriptid=scriptid, **params)
    
    def get(self, scriptid=None, **filters):
        """
        Retrieve scripts according to the given parameters.
        
        Args:
            scriptid (str|list, optional): Return only scripts with the given IDs.
            
        Keyword Args (filters):
            hostids (list, optional): Return only scripts that can be run on the given hosts.
            groupids (list, optional): Return only scripts that can be run on hosts in the given groups.
            usrgrpids (list, optional): Return only scripts available to the given user groups.
            selectHostGroups (str|list, optional): Include host groups in the result.
            selectHosts (str|list, optional): Include hosts in the result.
            filter (dict, optional): Filter scripts by given properties.
            search (dict, optional): Search scripts by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing scripts matching the criteria.
        
        Example:
            >>> # Get all scripts
            >>> scripts = zapi.scripts.get()
            >>> 
            >>> # Get scripts for a host
            >>> scripts = zapi.scripts.get(hostids=["10105"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/get
        """
        return self._call(f"{self.API_METHOD}.get", scriptid=scriptid, **filters)

    def get_scripts_by_events(self, **params):
        """
        Retrieve scripts available for execution on the given events.
        
        Keyword Args (params):
            eventids (list, required): Event IDs.
        
        Returns:
            dict: API response containing scripts available for the events.
        
        Example:
            >>> scripts = zapi.scripts.get_scripts_by_events(eventids=["12345"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/getscriptsbyevents
        """
        return self._call(f"{self.API_METHOD}.getscriptsbyevents", **params)
    
    def get_scripts_by_hosts(self, **params):
        """
        Retrieve scripts available for execution on the given hosts.
        
        Keyword Args (params):
            hostids (list, required): Host IDs.
        
        Returns:
            dict: API response containing scripts available for the hosts.
        
        Example:
            >>> scripts = zapi.scripts.get_scripts_by_hosts(hostids=["10105", "10106"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/getscriptsbyhosts
        """
        return self._call(f"{self.API_METHOD}.getscriptsbyshosts", **params)
        
    def update(self, scriptid, **params):
        """
        Update existing scripts.
        
        Args:
            scriptid (str): ID of the script to update.
            
        Keyword Args (params):
            name (str, optional): Name of the script.
            command (str, optional): Command to run.
            host_access (int, optional): Host permissions (0: no access, 2: read, 3: write).
            usrgrpid (str, optional): User group ID that will be used to run the script.
            groupid (str, optional): Host group ID where the script can be executed.
            description (str, optional): Description of the script.
            confirmation (str, optional): Confirmation text.
            type (int, optional): Script type.
            execute_on (int, optional): Where to run the script.
            timeout (str, optional): Script execution timeout.
            scope (int, optional): Script scope (0: action, 1: host, 2: event).
            menu_path (str, optional): Menu path for the script.
            parameters (list, optional): Script parameters.
        
        Returns:
            dict: API response containing the IDs of updated scripts.
        
        Example:
            >>> zapi.scripts.update(
            ...     scriptid="1",
            ...     name="Updated Script Name",
            ...     command="echo 'Updated'"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/update
        """
        return self._call(f"{self.API_METHOD}.update", scriptid=scriptid, **params)