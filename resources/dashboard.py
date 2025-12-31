# resources/dashboard.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/dashboard

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class DashboardResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "dashboard"

    def create(self, **params):
        """
        Create new dashboards.
        
        Keyword Args (params):
            name (str, required): Name of the dashboard.
            display_period (int, optional): Automatic refresh interval in seconds.
            auto_start (int, optional): Auto-start slideshow (0: disabled, 1: enabled).
            uuid (str, optional): Unique dashboard identifier.
            pages (list, required): Dashboard pages. Each object should contain dashboard_pageid, name, display_period, widgets.
            userid (str, optional): ID of the user who owns the dashboard.
            private (int, optional): Dashboard sharing (0: public, 1: private).
            users (list, optional): Users to share the dashboard with.
            user_groups (list, optional): User groups to share the dashboard with.
        
        Returns:
            dict: API response containing the IDs of created dashboards.
        
        Example:
            >>> dashboard = zapi.dashboards.create(
            ...     name="My Dashboard",
            ...     pages=[{
            ...         "name": "Page 1",
            ...         "widgets": []
            ...     }]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/dashboard/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, dashboardid):
        """
        Delete dashboards.
        
        Args:
            dashboardid (str|list): ID or list of IDs of dashboards to delete.
        
        Returns:
            dict: API response containing the IDs of deleted dashboards.
        
        Example:
            >>> # Delete a single dashboard
            >>> zapi.dashboards.delete(dashboardid="1")
            >>> 
            >>> # Delete multiple dashboards
            >>> zapi.dashboards.delete(dashboardid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/dashboard/delete
        """
        return self._call(f"{self.API_METHOD}.delete", dashboardid=dashboardid)

    def get(self, dashboardid=None, **filters):
        """
        Retrieve dashboards according to the given parameters.
        
        Args:
            dashboardid (str|list, optional): Return only dashboards with the given IDs.
            
        Keyword Args (filters):
            selectPages (str|list, optional): Include dashboard pages in the result.
            selectUsers (str|list, optional): Include users in the result.
            selectUserGroups (str|list, optional): Include user groups in the result.
            filter (dict, optional): Filter dashboards by given properties.
            search (dict, optional): Search dashboards by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing dashboards matching the criteria.
        
        Example:
            >>> # Get all dashboards
            >>> dashboards = zapi.dashboards.get()
            >>> 
            >>> # Get dashboard with pages
            >>> dashboard = zapi.dashboards.get(dashboardid="1", selectPages="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/dashboard/get
        """
        return self._call(f"{self.API_METHOD}.get", dashboardid=dashboardid, **filters)
    
    def update(self, dashboardid, **params):
        """
        Update existing dashboards.
        
        Args:
            dashboardid (str): ID of the dashboard to update.
            
        Keyword Args (params):
            name (str, optional): Name of the dashboard.
            display_period (int, optional): Automatic refresh interval in seconds.
            auto_start (int, optional): Auto-start slideshow (0: disabled, 1: enabled).
            uuid (str, optional): Unique dashboard identifier.
            pages (list, optional): Dashboard pages.
            userid (str, optional): ID of the user who owns the dashboard.
            private (int, optional): Dashboard sharing (0: public, 1: private).
            users (list, optional): Users to share the dashboard with.
            user_groups (list, optional): User groups to share the dashboard with.
        
        Returns:
            dict: API response containing the IDs of updated dashboards.
        
        Example:
            >>> zapi.dashboards.update(
            ...     dashboardid="1",
            ...     name="Updated Dashboard Name",
            ...     display_period=60
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/dashboard/update
        """
        return self._call(f"{self.API_METHOD}.update", dashboardid=dashboardid, **params)