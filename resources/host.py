# resources/host.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/host

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HostResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "host"

    def create(self, **params):
        """
        Create new hosts.
        
        Keyword Args (params):
            host (str, required): Technical name of the host.
            interfaces (list, required): Host interfaces to be created for the host.
                Each interface object should contain: type, main, useip, ip, dns, port
            groups (list, required): Host groups to add the host to. Each object should have a groupid.
            name (str, optional): Visible name of the host. Default: same as host.
            description (str, optional): Description of the host.
            inventory (dict, optional): Host inventory properties.
            inventory_mode (int, optional): Host inventory population mode.
                - -1: Disabled
                - 0: Manual
                - 1: Automatic
            ipmi_authtype (int, optional): IPMI authentication algorithm.
            ipmi_privilege (int, optional): IPMI privilege level.
            ipmi_username (str, optional): IPMI username.
            ipmi_password (str, optional): IPMI password.
            macros (list, optional): User macros to assign to the host.
            tags (list, optional): Tags to assign to the host.
            templates (list, optional): Templates to link to the host. Each object should have a templateid.
            tls_connect (int, optional): Connections to host.
            tls_accept (int, optional): Connections from host.
            tls_issuer (str, optional): Certificate issuer.
            tls_subject (str, optional): Certificate subject.
            tls_psk_identity (str, optional): PSK identity.
            tls_psk (str, optional): PSK value.
        
        Returns:
            dict: API response containing the IDs of created hosts.
        
        Example:
            >>> host = zapi.hosts.create(
            ...     host="test-host",
            ...     interfaces=[{
            ...         "type": 1,
            ...         "main": 1,
            ...         "useip": 1,
            ...         "ip": "127.0.0.1",
            ...         "dns": "",
            ...         "port": "10050"
            ...     }],
            ...     groups=[{"groupid": "1"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/host/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, hostid):
        """
        Delete hosts.
        
        Args:
            hostid (str|list): ID or list of IDs of hosts to delete.
        
        Returns:
            dict: API response containing the IDs of deleted hosts.
        
        Example:
            >>> # Delete a single host
            >>> zapi.hosts.delete(hostid="10105")
            >>> 
            >>> # Delete multiple hosts
            >>> zapi.hosts.delete(hostid=["10105", "10106"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/host/delete
        """
        return self._call(f"{self.API_METHOD}.delete", hostid=hostid)

    def get(self, hostid=None, **filters):
        """
        Retrieve hosts according to the given parameters.
        
        Args:
            hostid (str|list, optional): Return only hosts with the given IDs.
            
        Keyword Args (filters):
            groupids (list, optional): Return only hosts that belong to the given host groups.
            templateids (list, optional): Return only hosts that are linked to the given templates.
            proxyids (list, optional): Return only hosts that are monitored by the given proxies.
            selectGroups (str|list, optional): Include host groups in the result.
                - "extend": Include all host group properties
                - list: Return only the specified properties
            selectParentTemplates (str|list, optional): Include parent templates in the result.
            selectInterfaces (str|list, optional): Include host interfaces in the result.
                - "extend": Include all interface properties
                - list: Return only the specified properties
            selectItems (str|list, optional): Include items in the result.
            selectDiscoveries (str|list, optional): Include discovery rules in the result.
            selectTriggers (str|list, optional): Include triggers in the result.
            selectGraphs (str|list, optional): Include graphs in the result.
            selectApplications (str|list, optional): Include applications in the result.
            selectMacros (str|list, optional): Include macros in the result.
            selectScreens (str|list, optional): Include screens in the result.
            selectHttpTests (str|list, optional): Include web scenarios in the result.
            selectTags (str|list, optional): Include tags in the result.
            selectInheritedTags (str|list, optional): Include inherited tags in the result.
            selectInventory (str|bool, optional): Include host inventory in the result.
            selectDashboards (str|list, optional): Include dashboards in the result.
            filter (dict, optional): Filter hosts by given properties.
                Example: filter={"status": "0", "host": "Zabbix server"}
            search (dict, optional): Search hosts by given properties (case-insensitive).
            searchInventory (dict, optional): Search host inventory by given properties.
            output (str|list, optional): Object properties to be returned.
                - "extend": Return all properties
                - list: Return only the specified properties
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing hosts matching the criteria.
        
        Example:
            >>> # Get all hosts with interfaces
            >>> hosts = zapi.hosts.get(selectInterfaces="extend")
            >>> 
            >>> # Get hosts by group ID with items
            >>> hosts = zapi.hosts.get(groupids=["1"], selectItems="extend")
            >>> 
            >>> # Filter hosts by status
            >>> active_hosts = zapi.hosts.get(filter={"status": "0"})
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/host/get
        """
        return self._call(f"{self.API_METHOD}.get", hostid=hostid, **filters)
    
    def massadd(self, **params):
        """
        Mass add related objects to hosts.
        
        Keyword Args (params):
            hosts (list, required): Hosts to update. Each object should have a hostid.
            groups (list, optional): Host groups to add the hosts to.
            templates (list, optional): Templates to link to the hosts.
            macros (list, optional): Macros to add to the hosts.
            hosts_templates (list, optional): Templates to link/unlink to the hosts.
                Each object should have hostid and templates (list of templateid).
        
        Returns:
            dict: API response containing the IDs of updated hosts.
        
        Example:
            >>> zapi.hosts.massadd(
            ...     hosts=[{"hostid": "10105"}],
            ...     groups=[{"groupid": "2"}],
            ...     templates=[{"templateid": "10001"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/host/massadd
        """
        return self._call(f"{self.API_METHOD}.massadd", **params)

    def massremove(self, **params):
        """
        Mass remove related objects from hosts.
        
        Keyword Args (params):
            hostids (list, required): IDs of hosts to update.
            groupids (list, optional): Host groups to remove the hosts from.
            templateids (list, optional): Templates to unlink from the hosts.
            templateids_clear (list, optional): Templates to unlink and clear from the hosts.
            macros (list, optional): Macros to remove from the hosts.
        
        Returns:
            dict: API response containing the IDs of updated hosts.
        
        Example:
            >>> zapi.hosts.massremove(
            ...     hostids=["10105", "10106"],
            ...     groupids=["2"],
            ...     templateids=["10001"]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/host/massremove
        """
        return self._call(f"{self.API_METHOD}.massremove", **params)

    def massupdate(self, **params):
        """
        Mass update hosts, replacing or removing related objects.
        
        Keyword Args (params):
            hosts (list, required): Hosts to update. Each object should have a hostid.
            groups (list, optional): Host groups to replace existing ones.
            templates (list, optional): Templates to replace existing ones.
            templates_clear (list, optional): Templates to unlink from the hosts.
            macros (list, optional): Macros to replace existing ones.
            tags (list, optional): Tags to replace existing ones.
            inventory (dict, optional): Host inventory to update.
            inventory_mode (int, optional): Host inventory population mode.
            status (int, optional): Status of the host (0: enabled, 1: disabled).
            interfaces (list, optional): Interfaces to update.
        
        Returns:
            dict: API response containing the IDs of updated hosts.
        
        Example:
            >>> zapi.hosts.massupdate(
            ...     hosts=[{"hostid": "10105"}],
            ...     status=1,
            ...     groups=[{"groupid": "2"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/host/massupdate
        """
        return self._call(f"{self.API_METHOD}.massupdate", **params)

    def update(self, hostid, **params):
        """
        Update existing hosts.
        
        Args:
            hostid (str): ID of the host to update.
            
        Keyword Args (params):
            host (str, optional): Technical name of the host.
            name (str, optional): Visible name of the host.
            interfaces (list, optional): Host interfaces to update.
            groups (list, optional): Host groups to replace existing ones.
            templates (list, optional): Templates to replace existing ones.
            templates_clear (list, optional): Templates to unlink from the host.
            macros (list, optional): Macros to replace existing ones.
            tags (list, optional): Tags to replace existing ones.
            inventory (dict, optional): Host inventory properties to update.
            inventory_mode (int, optional): Host inventory population mode.
            ipmi_authtype (int, optional): IPMI authentication algorithm.
            ipmi_privilege (int, optional): IPMI privilege level.
            ipmi_username (str, optional): IPMI username.
            ipmi_password (str, optional): IPMI password.
            status (int, optional): Status of the host (0: enabled, 1: disabled).
            description (str, optional): Description of the host.
            tls_connect (int, optional): Connections to host.
            tls_accept (int, optional): Connections from host.
            tls_issuer (str, optional): Certificate issuer.
            tls_subject (str, optional): Certificate subject.
            tls_psk_identity (str, optional): PSK identity.
            tls_psk (str, optional): PSK value.
        
        Returns:
            dict: API response containing the IDs of updated hosts.
        
        Example:
            >>> zapi.hosts.update(
            ...     hostid="10105",
            ...     name="Updated Host Name",
            ...     status=1
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/host/update
        """
        return self._call(f"{self.API_METHOD}.update", hostid=hostid, **params)