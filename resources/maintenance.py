# resources/maintenance.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/maintenance

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class MaintenanceResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "maintenance"

    def create(self, **params):
        """
        Create new maintenance periods.
        
        Keyword Args (params):
            name (str, required): Name of the maintenance period.
            active_since (int, required): Maintenance start time (Unix timestamp).
            active_till (int, required): Maintenance end time (Unix timestamp).
            description (str, optional): Description of the maintenance period.
            maintenance_type (int, optional): Type of maintenance (0: with data collection, 1: without data collection).
            tags_evaltype (int, optional): Tag evaluation method (0: AND/OR, 1: OR).
            tags (list, optional): Maintenance tags.
            timeperiods (list, required): Maintenance time periods. Each object should contain timeperiod_type, every, dayofweek, day, start_time, period.
            groupids (list, optional): Host groups to include in maintenance. Each object should have a groupid.
            hostids (list, optional): Hosts to include in maintenance. Each object should have a hostid.
        
        Returns:
            dict: API response containing the IDs of created maintenance periods.
        
        Example:
            >>> maintenance = zapi.maintenances.create(
            ...     name="Weekly Maintenance",
            ...     active_since=timestamp,
            ...     active_till=timestamp_end,
            ...     timeperiods=[{
            ...         "timeperiod_type": 0,
            ...         "start_time": 64800,
            ...         "period": 3600
            ...     }],
            ...     groupids=[{"groupid": "1"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/maintenance/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, maintenanceid):
        """
        Delete maintenance periods.
        
        Args:
            maintenanceid (str|list): ID or list of IDs of maintenance periods to delete.
        
        Returns:
            dict: API response containing the IDs of deleted maintenance periods.
        
        Example:
            >>> # Delete a single maintenance
            >>> zapi.maintenances.delete(maintenanceid="1")
            >>> 
            >>> # Delete multiple maintenances
            >>> zapi.maintenances.delete(maintenanceid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/maintenance/delete
        """
        return self._call(f"{self.API_METHOD}.delete", maintenanceid=maintenanceid)
    
    def get(self, maintenanceid=None, **filters):
        """
        Retrieve maintenance periods according to the given parameters.
        
        Args:
            maintenanceid (str|list, optional): Return only maintenance periods with the given IDs.
            
        Keyword Args (filters):
            groupids (list, optional): Return only maintenance periods that apply to the given host groups.
            hostids (list, optional): Return only maintenance periods that apply to the given hosts.
            selectGroups (str|list, optional): Include host groups in the result.
            selectHosts (str|list, optional): Include hosts in the result.
            selectTags (str|list, optional): Include tags in the result.
            selectTimeperiods (str|list, optional): Include time periods in the result.
            filter (dict, optional): Filter maintenance periods by given properties.
            search (dict, optional): Search maintenance periods by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing maintenance periods matching the criteria.
        
        Example:
            >>> # Get all maintenance periods
            >>> maintenances = zapi.maintenances.get()
            >>> 
            >>> # Get maintenance periods for a host group
            >>> maintenances = zapi.maintenances.get(groupids=["1"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/maintenance/get
        """
        return self._call(f"{self.API_METHOD}.get", maintenanceid=maintenanceid, **filters)
    
    def update(self, maintenanceid, **params):
        """
        Update existing maintenance periods.
        
        Args:
            maintenanceid (str): ID of the maintenance period to update.
            
        Keyword Args (params):
            name (str, optional): Name of the maintenance period.
            active_since (int, optional): Maintenance start time (Unix timestamp).
            active_till (int, optional): Maintenance end time (Unix timestamp).
            description (str, optional): Description of the maintenance period.
            maintenance_type (int, optional): Type of maintenance (0: with data collection, 1: without data collection).
            tags_evaltype (int, optional): Tag evaluation method (0: AND/OR, 1: OR).
            tags (list, optional): Maintenance tags.
            timeperiods (list, optional): Maintenance time periods.
            groupids (list, optional): Host groups to include in maintenance.
            hostids (list, optional): Hosts to include in maintenance.
        
        Returns:
            dict: API response containing the IDs of updated maintenance periods.
        
        Example:
            >>> zapi.maintenances.update(
            ...     maintenanceid="1",
            ...     name="Updated Maintenance Name",
            ...     active_till=new_timestamp
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/maintenance/update
        """
        return self._call(f"{self.API_METHOD}.update", maintenanceid=maintenanceid, **params)