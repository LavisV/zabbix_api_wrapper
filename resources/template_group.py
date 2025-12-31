# resources/template_group.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templategroup

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TemplateGroupResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "templategroup"
    
    def create(self, **params):
        """
        Create new template groups.
        
        Keyword Args (params):
            name (str, required): Name of the template group.
        
        Returns:
            dict: API response containing the IDs of created template groups.
        
        Example:
            >>> template_group = zapi.template_groups.create(name="Linux Templates")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templategroup/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, templategroupid):
        """
        Delete template groups.
        
        Args:
            templategroupid (str|list): ID or list of IDs of template groups to delete.
        
        Returns:
            dict: API response containing the IDs of deleted template groups.
        
        Example:
            >>> # Delete a single template group
            >>> zapi.template_groups.delete(templategroupid="1")
            >>> 
            >>> # Delete multiple template groups
            >>> zapi.template_groups.delete(templategroupid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templategroup/delete
        """
        return self._call(f"{self.API_METHOD}.delete", templategroupid=templategroupid)

    def get(self, templategroupid=None, **filters):
        """
        Retrieve template groups according to the given parameters.
        
        Args:
            templategroupid (str|list, optional): Return only template groups with the given IDs.
            
        Keyword Args (filters):
            templateids (list, optional): Return only template groups that contain the given templates.
            selectTemplates (str|list, optional): Include templates in the result.
            filter (dict, optional): Filter template groups by given properties.
            search (dict, optional): Search template groups by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing template groups matching the criteria.
        
        Example:
            >>> # Get all template groups
            >>> template_groups = zapi.template_groups.get()
            >>> 
            >>> # Get template groups with templates
            >>> template_groups = zapi.template_groups.get(selectTemplates="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templategroup/get
        """
        return self._call(f"{self.API_METHOD}.get", templategroupid=templategroupid, **filters)

    def mass_add(self, **params):
        """
        Mass add related objects to template groups.
        
        Keyword Args (params):
            groups (list, required): Template groups to update. Each object should have a groupid.
            templates (list, optional): Templates to add to the template groups.
        
        Returns:
            dict: API response containing the IDs of updated template groups.
        
        Example:
            >>> zapi.template_groups.mass_add(
            ...     groups=[{"groupid": "1"}],
            ...     templates=[{"templateid": "10001"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templategroup/massadd
        """
        return self._call(f"{self.API_METHOD}.massadd", **params)

    def mass_remove(self, **params):
        """
        Mass remove related objects from template groups.
        
        Keyword Args (params):
            groupids (list, required): IDs of template groups to update.
            templateids (list, optional): Templates to remove from the template groups.
        
        Returns:
            dict: API response containing the IDs of updated template groups.
        
        Example:
            >>> zapi.template_groups.mass_remove(
            ...     groupids=["1"],
            ...     templateids=["10001"]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templategroup/massremove
        """
        return self._call(f"{self.API_METHOD}.massremove", **params)

    def mass_update(self, **params):
        """
        Mass update template groups, replacing related objects.
        
        Keyword Args (params):
            groups (list, required): Template groups to update. Each object should have a groupid.
            templates (list, optional): Templates to replace existing ones.
        
        Returns:
            dict: API response containing the IDs of updated template groups.
        
        Example:
            >>> zapi.template_groups.mass_update(
            ...     groups=[{"groupid": "1"}],
            ...     templates=[{"templateid": "10001"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templategroup/massupdate
        """
        return self._call(f"{self.API_METHOD}.massupdate", **params)

    def propagate(self, **params):
        """
        Propagate template group permissions to all child groups.
        
        Keyword Args (params):
            groups (list, required): Template groups to propagate. Each object should have a groupid.
            permissions (dict, optional): Permissions to propagate.
        
        Returns:
            dict: API response confirming the propagation.
        
        Example:
            >>> zapi.template_groups.propagate(
            ...     groups=[{"groupid": "1"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templategroup/propagate
        """
        return self._call(f"{self.API_METHOD}.propagate", **params)
    
    def update(self, templategroupid, **params):
        """
        Update existing template groups.
        
        Args:
            templategroupid (str): ID of the template group to update.
            
        Keyword Args (params):
            name (str, optional): Name of the template group.
        
        Returns:
            dict: API response containing the IDs of updated template groups.
        
        Example:
            >>> zapi.template_groups.update(templategroupid="1", name="Updated Template Group Name")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templategroup/update
        """
        return self._call(f"{self.API_METHOD}.update", templategroupid=templategroupid, **params)