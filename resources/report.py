# resources/report.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/report

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ReportResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "report"

    def create(self, **params):
        """
        Create new reports.
        
        Keyword Args (params):
            name (str, required): Name of the report.
            dashboardid (str, required): ID of the dashboard to use for the report.
            period (int, required): Report period in seconds.
            cycle (str, required): Report cycle (daily, weekly, monthly, yearly).
            start_time (int, required): Report start time (Unix timestamp).
            subject (str, required): Email subject.
            recipients (list, required): Report recipients. Each object should have usrgrpid, userid, or roleid.
            status (int, optional): Whether the report is enabled (0: disabled, 1: enabled).
            description (str, optional): Description of the report.
            active_since (int, optional): Report active since timestamp.
            active_till (int, optional): Report active until timestamp.
            info (dict, optional): Report generation information.
        
        Returns:
            dict: API response containing the IDs of created reports.
        
        Example:
            >>> report = zapi.reports.create(
            ...     name="Weekly Report",
            ...     dashboardid="1",
            ...     period=604800,
            ...     cycle="weekly",
            ...     start_time=timestamp,
            ...     subject="Weekly Monitoring Report",
            ...     recipients=[{"usrgrpid": "7"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/report/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, reportid):
        """
        Delete reports.
        
        Args:
            reportid (str|list): ID or list of IDs of reports to delete.
        
        Returns:
            dict: API response containing the IDs of deleted reports.
        
        Example:
            >>> # Delete a single report
            >>> zapi.reports.delete(reportid="1")
            >>> 
            >>> # Delete multiple reports
            >>> zapi.reports.delete(reportid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/report/delete
        """
        return self._call(f"{self.API_METHOD}.delete", reportid=reportid)

    def get(self, reportid=None, **filters):
        """
        Retrieve reports according to the given parameters.
        
        Args:
            reportid (str|list, optional): Return only reports with the given IDs.
            
        Keyword Args (filters):
            selectUsers (str|list, optional): Include users in the result.
            selectUserGroups (str|list, optional): Include user groups in the result.
            selectRoles (str|list, optional): Include roles in the result.
            filter (dict, optional): Filter reports by given properties.
            search (dict, optional): Search reports by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing reports matching the criteria.
        
        Example:
            >>> # Get all reports
            >>> reports = zapi.reports.get()
            >>> 
            >>> # Get report by ID
            >>> report = zapi.reports.get(reportid="1")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/report/get
        """
        return self._call(f"{self.API_METHOD}.get", reportid=reportid, **filters)
    
    def update(self, reportid, **params):
        """
        Update existing reports.
        
        Args:
            reportid (str): ID of the report to update.
            
        Keyword Args (params):
            name (str, optional): Name of the report.
            dashboardid (str, optional): ID of the dashboard to use for the report.
            period (int, optional): Report period in seconds.
            cycle (str, optional): Report cycle (daily, weekly, monthly, yearly).
            start_time (int, optional): Report start time (Unix timestamp).
            subject (str, optional): Email subject.
            recipients (list, optional): Report recipients.
            status (int, optional): Whether the report is enabled (0: disabled, 1: enabled).
            description (str, optional): Description of the report.
            active_since (int, optional): Report active since timestamp.
            active_till (int, optional): Report active until timestamp.
            info (dict, optional): Report generation information.
        
        Returns:
            dict: API response containing the IDs of updated reports.
        
        Example:
            >>> zapi.reports.update(
            ...     reportid="1",
            ...     name="Updated Report Name",
            ...     status=1
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/report/update
        """
        return self._call(f"{self.API_METHOD}.update", reportid=reportid, **params)