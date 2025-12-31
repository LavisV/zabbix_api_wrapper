# resources/host_group.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostgroup

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HostGroupResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "hostgroup"

    def create(self, **params):
        """
        Create new host groups.
        
        Keyword Args (params):
            name (str, required): Name of the host group.
        
        Returns:
            dict: API response containing the IDs of created host groups.
        
        Example:
            >>> group = zapi.host_groups.create(name="Linux Servers")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostgroup/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, groupid):
        """
        Delete host groups.
        
        Args:
            groupid (str|list): ID or list of IDs of host groups to delete.
        
        Returns:
            dict: API response containing the IDs of deleted host groups.
        
        Example:
            >>> # Delete a single host group
            >>> zapi.host_groups.delete(groupid="1")
            >>> 
            >>> # Delete multiple host groups
            >>> zapi.host_groups.delete(groupid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostgroup/delete
        """
        return self._call(f"{self.API_METHOD}.delete", groupid=groupid)

    def get(self, **params):
        """
        Retrieve host groups according to the given parameters.
        
        Keyword Args (params):
            groupids (list, optional): Return only host groups with the given IDs.
            hostids (list, optional): Return only host groups that contain the given hosts.
            templateids (list, optional): Return only host groups that contain the given templates.
            monitored_hosts (bool, optional): Return only host groups that contain monitored hosts.
            real_hosts (bool, optional): Return only host groups that contain real hosts (not templates).
            with_hosts_and_templates (bool, optional): Return only host groups that contain hosts or templates.
            selectHosts (str|list, optional): Include hosts in the result.
            selectTemplates (str|list, optional): Include templates in the result.
            filter (dict, optional): Filter host groups by given properties.
            search (dict, optional): Search host groups by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing host groups matching the criteria.
        
        Example:
            >>> # Get all host groups
            >>> groups = zapi.host_groups.get()
            >>> 
            >>> # Get host groups with hosts
            >>> groups = zapi.host_groups.get(selectHosts="extend")
            >>> 
            >>> # Get host groups containing monitored hosts
            >>> groups = zapi.host_groups.get(monitored_hosts=True)
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostgroup/get
        """
        return self._call(f"{self.API_METHOD}.get", **params)

    def massadd(self, **params):
        """
        Mass add related objects to host groups.
        
        Keyword Args (params):
            groups (list, required): Host groups to update. Each object should have a groupid.
            hosts (list, optional): Hosts to add to the host groups.
            templates (list, optional): Templates to add to the host groups.
        
        Returns:
            dict: API response containing the IDs of updated host groups.
        
        Example:
            >>> zapi.host_groups.massadd(
            ...     groups=[{"groupid": "1"}],
            ...     hosts=[{"hostid": "10105"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostgroup/massadd
        """
        return self._call(f"{self.API_METHOD}.massadd", **params)

    def massremove(self, **params):
        """
        Mass remove related objects from host groups.
        
        Keyword Args (params):
            groupids (list, required): IDs of host groups to update.
            hostids (list, optional): Hosts to remove from the host groups.
            templateids (list, optional): Templates to remove from the host groups.
        
        Returns:
            dict: API response containing the IDs of updated host groups.
        
        Example:
            >>> zapi.host_groups.massremove(
            ...     groupids=["1"],
            ...     hostids=["10105"]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostgroup/massremove
        """
        return self._call(f"{self.API_METHOD}.massremove", **params)

    def massupdate(self, **params):
        """
        Mass update host groups, replacing related objects.
        
        Keyword Args (params):
            groups (list, required): Host groups to update. Each object should have a groupid.
            hosts (list, optional): Hosts to replace existing ones.
            templates (list, optional): Templates to replace existing ones.
        
        Returns:
            dict: API response containing the IDs of updated host groups.
        
        Example:
            >>> zapi.host_groups.massupdate(
            ...     groups=[{"groupid": "1"}],
            ...     hosts=[{"hostid": "10105"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostgroup/massupdate
        """
        return self._call(f"{self.API_METHOD}.massupdate", **params)

    def update(self, groupid, **params):
        """
        Update existing host groups.
        
        Args:
            groupid (str): ID of the host group to update.
            
        Keyword Args (params):
            name (str, optional): Name of the host group.
        
        Returns:
            dict: API response containing the IDs of updated host groups.
        
        Example:
            >>> zapi.host_groups.update(groupid="1", name="Updated Group Name")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostgroup/update
        """
        return self._call(f"{self.API_METHOD}.update", groupid=groupid, **params)