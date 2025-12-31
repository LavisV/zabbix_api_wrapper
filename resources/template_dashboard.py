# resources/template_dashboard.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templatedashboard

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TemplateDashboardResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "templatedashboard"

    def create(self, **params):
        """
        Create new template dashboards.
        
        Keyword Args (params):
            name (str, required): Name of the template dashboard.
            templateid (str, required): ID of the template that the dashboard belongs to.
            display_period (int, optional): Automatic refresh interval in seconds.
            auto_start (int, optional): Auto-start slideshow (0: disabled, 1: enabled).
            uuid (str, optional): Unique dashboard identifier.
            pages (list, required): Dashboard pages. Each object should contain dashboard_pageid, name, display_period, widgets.
        
        Returns:
            dict: API response containing the IDs of created template dashboards.
        
        Example:
            >>> template_dashboard = zapi.template_dashboards.create(
            ...     name="Template Dashboard",
            ...     templateid="10001",
            ...     pages=[{
            ...         "name": "Page 1",
            ...         "widgets": []
            ...     }]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templatedashboard/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, templatedashboardid):
        """
        Delete template dashboards.
        
        Args:
            templatedashboardid (str|list): ID or list of IDs of template dashboards to delete.
        
        Returns:
            dict: API response containing the IDs of deleted template dashboards.
        
        Example:
            >>> # Delete a single template dashboard
            >>> zapi.template_dashboards.delete(templatedashboardid="1")
            >>> 
            >>> # Delete multiple template dashboards
            >>> zapi.template_dashboards.delete(templatedashboardid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templatedashboard/delete
        """
        return self._call(f"{self.API_METHOD}.delete", templatedashboardid=templatedashboardid)

    def get(self, templatedashboardid=None, **filters):
        """
        Retrieve template dashboards according to the given parameters.
        
        Args:
            templatedashboardid (str|list, optional): Return only template dashboards with the given IDs.
            
        Keyword Args (filters):
            templateids (list, optional): Return only template dashboards that belong to the given templates.
            selectPages (str|list, optional): Include dashboard pages in the result.
            filter (dict, optional): Filter template dashboards by given properties.
            search (dict, optional): Search template dashboards by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing template dashboards matching the criteria.
        
        Example:
            >>> # Get all template dashboards
            >>> template_dashboards = zapi.template_dashboards.get()
            >>> 
            >>> # Get template dashboards for a template
            >>> template_dashboards = zapi.template_dashboards.get(templateids=["10001"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templatedashboard/get
        """
        return self._call(f"{self.API_METHOD}.get", templatedashboardid=templatedashboardid, **filters)
    
    def update(self, templatedashboardid, **params):
        """
        Update existing template dashboards.
        
        Args:
            templatedashboardid (str): ID of the template dashboard to update.
            
        Keyword Args (params):
            name (str, optional): Name of the template dashboard.
            templateid (str, optional): ID of the template that the dashboard belongs to.
            display_period (int, optional): Automatic refresh interval in seconds.
            auto_start (int, optional): Auto-start slideshow (0: disabled, 1: enabled).
            uuid (str, optional): Unique dashboard identifier.
            pages (list, optional): Dashboard pages.
        
        Returns:
            dict: API response containing the IDs of updated template dashboards.
        
        Example:
            >>> zapi.template_dashboards.update(
            ...     templatedashboardid="1",
            ...     name="Updated Template Dashboard Name",
            ...     display_period=60
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/templatedashboard/update
        """
        return self._call(f"{self.API_METHOD}.update", templatedashboardid=templatedashboardid, **params)