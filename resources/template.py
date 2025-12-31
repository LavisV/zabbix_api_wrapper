# resources/template.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/template

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TemplateResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "template"

    def create(self, **params):
        """
        Create new templates.
        
        Keyword Args (params):
            host (str, required): Technical name of the template.
            groups (list, required): Template groups to add the template to. Each object should have a groupid.
            name (str, optional): Visible name of the template.
            description (str, optional): Description of the template.
            tags (list, optional): Tags to assign to the template.
            macros (list, optional): User macros to assign to the template.
        
        Returns:
            dict: API response containing the IDs of created templates.
        
        Example:
            >>> template = zapi.templates.create(
            ...     host="Template OS Linux",
            ...     groups=[{"groupid": "1"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/template/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, templateid):
        """
        Delete templates.
        
        Args:
            templateid (str|list): ID or list of IDs of templates to delete.
        
        Returns:
            dict: API response containing the IDs of deleted templates.
        
        Example:
            >>> # Delete a single template
            >>> zapi.templates.delete(templateid="10001")
            >>> 
            >>> # Delete multiple templates
            >>> zapi.templates.delete(templateid=["10001", "10002"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/template/delete
        """
        return self._call(f"{self.API_METHOD}.delete", templateid=templateid)

    def get(self, templateid=None, **filters):
        """
        Retrieve templates according to the given parameters.
        
        Args:
            templateid (str|list, optional): Return only templates with the given IDs.
            
        Keyword Args (filters):
            groupids (list, optional): Return only templates that belong to the given template groups.
            parentTemplateids (list, optional): Return only templates that are children of the given templates.
            hostids (list, optional): Return only templates that are linked to the given hosts.
            graphids (list, optional): Return only templates that contain the given graphs.
            itemids (list, optional): Return only templates that contain the given items.
            triggerids (list, optional): Return only templates that contain the given triggers.
            with_items (bool, optional): Return only templates that contain items.
            with_graphs (bool, optional): Return only templates that contain graphs.
            with_httptests (bool, optional): Return only templates that contain web scenarios.
            evaltype (int, optional): Rules for tag evaluation.
            tags (list, optional): Return only templates with given tags.
            selectGroups (str|list, optional): Include template groups in the result.
            selectHosts (str|list, optional): Include linked hosts in the result.
            selectTemplates (str|list, optional): Include parent templates in the result.
            selectParentTemplates (str|list, optional): Include parent templates in the result.
            selectHttpTests (str|list, optional): Include web scenarios in the result.
            selectItems (str|list, optional): Include items in the result.
            selectDiscoveries (str|list, optional): Include discovery rules in the result.
            selectTriggers (str|list, optional): Include triggers in the result.
            selectGraphs (str|list, optional): Include graphs in the result.
            selectApplications (str|list, optional): Include applications in the result.
            selectMacros (str|list, optional): Include macros in the result.
            selectTags (str|list, optional): Include tags in the result.
            selectDashboards (str|list, optional): Include dashboards in the result.
            filter (dict, optional): Filter templates by given properties.
            search (dict, optional): Search templates by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing templates matching the criteria.
        
        Example:
            >>> # Get all templates
            >>> templates = zapi.templates.get()
            >>> 
            >>> # Get templates by group
            >>> templates = zapi.templates.get(groupids=["1"])
            >>> 
            >>> # Get templates with items
            >>> templates = zapi.templates.get(with_items=True)
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/template/get
        """
        return self._call(f"{self.API_METHOD}.get", templateid=templateid, **filters)

    def mass_add(self, **params):
        """
        Mass add related objects to templates.
        
        Keyword Args (params):
            templates (list, required): Templates to update. Each object should have a templateid.
            groups (list, optional): Template groups to add the templates to.
            hosts (list, optional): Hosts to link the templates to.
            templates_link (list, optional): Templates to link as parent templates.
            macros (list, optional): Macros to add to the templates.
        
        Returns:
            dict: API response containing the IDs of updated templates.
        
        Example:
            >>> zapi.templates.mass_add(
            ...     templates=[{"templateid": "10001"}],
            ...     groups=[{"groupid": "2"}],
            ...     hosts=[{"hostid": "10105"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/template/massadd
        """
        return self._call(f"{self.API_METHOD}.massadd", **params)

    def mass_remove(self, **params):
        """
        Mass remove related objects from templates.
        
        Keyword Args (params):
            templateids (list, required): IDs of templates to update.
            groupids (list, optional): Template groups to remove the templates from.
            hostids (list, optional): Hosts to unlink the templates from.
            templateids_clear (list, optional): Parent templates to unlink and clear from the templates.
            macros (list, optional): Macros to remove from the templates.
        
        Returns:
            dict: API response containing the IDs of updated templates.
        
        Example:
            >>> zapi.templates.mass_remove(
            ...     templateids=["10001", "10002"],
            ...     groupids=["2"]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/template/massremove
        """
        return self._call(f"{self.API_METHOD}.massremove", **params)

    def mass_update(self, **params):
        """
        Mass update templates, replacing or removing related objects.
        
        Keyword Args (params):
            templates (list, required): Templates to update. Each object should have a templateid.
            groups (list, optional): Template groups to replace existing ones.
            templates_link (list, optional): Parent templates to link.
            templates_clear (list, optional): Parent templates to unlink from the templates.
            macros (list, optional): Macros to replace existing ones.
            tags (list, optional): Tags to replace existing ones.
        
        Returns:
            dict: API response containing the IDs of updated templates.
        
        Example:
            >>> zapi.templates.mass_update(
            ...     templates=[{"templateid": "10001"}],
            ...     groups=[{"groupid": "2"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/template/massupdate
        """
        return self._call(f"{self.API_METHOD}.massupdate", **params)
    
    def update(self, templateid, **params):
        """
        Update existing templates.
        
        Args:
            templateid (str): ID of the template to update.
            
        Keyword Args (params):
            host (str, optional): Technical name of the template.
            name (str, optional): Visible name of the template.
            description (str, optional): Description of the template.
            groups (list, optional): Template groups to replace existing ones.
            templates_link (list, optional): Parent templates to link.
            templates_clear (list, optional): Parent templates to unlink from the template.
            macros (list, optional): Macros to replace existing ones.
            tags (list, optional): Tags to replace existing ones.
        
        Returns:
            dict: API response containing the IDs of updated templates.
        
        Example:
            >>> zapi.templates.update(
            ...     templateid="10001",
            ...     name="Updated Template Name"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/template/update
        """
        return self._call(f"{self.API_METHOD}.update", templateid=templateid, **params)