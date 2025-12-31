# resources/trigger.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/trigger

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TriggerResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "trigger"

    def create(self, **params):
        """
        Create new triggers.
        
        Keyword Args (params):
            description (str, required): Name of the trigger.
            expression (str, required): Reduced trigger expression.
            event_name (str, optional): Event name generation method.
            opdata (str, optional): Operational data to display with trigger name.
            comments (str, optional): Trigger comments.
            priority (int, optional): Severity of the trigger (0-5).
            status (int, optional): Whether the trigger is enabled (0: enabled, 1: disabled).
            type (int, optional): Type of the trigger (0: normal, 1: multiple).
            recover_mode (int, optional): OK event generation mode.
            corr_mode (int, optional): Correlation mode.
            corr_conditionid (str, optional): ID of the correlation rule.
            manual_close (int, optional): Allow manual close (0: no, 1: yes).
            tags (list, optional): Trigger tags.
            dependencies (list, optional): Trigger dependencies. Each object should have a triggerid.
        
        Returns:
            dict: API response containing the IDs of created triggers.
        
        Example:
            >>> trigger = zapi.triggers.create(
            ...     description="High CPU usage",
            ...     expression="{host:system.cpu.util.avg(5m)}>80",
            ...     priority=3
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/trigger/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, triggerid):
        """
        Delete triggers.
        
        Args:
            triggerid (str|list): ID or list of IDs of triggers to delete.
        
        Returns:
            dict: API response containing the IDs of deleted triggers.
        
        Example:
            >>> # Delete a single trigger
            >>> zapi.triggers.delete(triggerid="12345")
            >>> 
            >>> # Delete multiple triggers
            >>> zapi.triggers.delete(triggerid=["12345", "12346"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/trigger/delete
        """
        return self._call(f"{self.API_METHOD}.delete", triggerid=triggerid)

    def get(self, triggerid=None, **filters):
        """
        Retrieve triggers according to the given parameters.
        
        Args:
            triggerid (str|list, optional): Return only triggers with the given IDs.
            
        Keyword Args (filters):
            groupids (list, optional): Return only triggers that belong to the given host groups.
            templateids (list, optional): Return only triggers that belong to the given templates.
            hostids (list, optional): Return only triggers that belong to the given hosts.
            itemids (list, optional): Return only triggers that contain the given items.
            functions (list, optional): Return only triggers that use the given functions.
            monitored (bool, optional): Return only enabled triggers that belong to monitored hosts.
            active (bool, optional): Return only enabled triggers.
            maintenance (bool, optional): Return only triggers in maintenance state.
            withUnacknowledgedEvents (bool, optional): Return only triggers with unacknowledged events.
            withAcknowledgedEvents (bool, optional): Return only triggers with acknowledged events.
            withLastEventUnacknowledged (bool, optional): Return only triggers with last event unacknowledged.
            skipDependent (bool, optional): Skip dependent triggers.
            only_true (bool, optional): Return only currently active triggers.
            min_severity (int, optional): Return only triggers with severity greater than or equal to this value.
            evaltype (int, optional): Rules for tag evaluation.
            tags (list, optional): Return only triggers with given tags.
            expandDescription (bool, optional): Expand macros in trigger description.
            expandComment (bool, optional): Expand macros in trigger comments.
            expandExpression (bool, optional): Expand macros in trigger expression.
            selectGroups (str|list, optional): Include host groups in the result.
            selectHosts (str|list, optional): Include hosts in the result.
            selectItems (str|list, optional): Include items in the result.
            selectFunctions (str|list, optional): Include functions in the result.
            selectDependencies (str|list, optional): Include dependencies in the result.
            selectDiscoveryRule (str|list, optional): Include LLD rule in the result.
            selectLastEvent (str|list, optional): Include last event in the result.
            selectTags (str|list, optional): Include tags in the result.
            filter (dict, optional): Filter triggers by given properties.
            search (dict, optional): Search triggers by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing triggers matching the criteria.
        
        Example:
            >>> # Get all triggers
            >>> triggers = zapi.triggers.get()
            >>> 
            >>> # Get triggers by host
            >>> triggers = zapi.triggers.get(hostids=["10105"])
            >>> 
            >>> # Get active triggers with high severity
            >>> triggers = zapi.triggers.get(active=True, min_severity=4)
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/trigger/get
        """
        return self._call(f"{self.API_METHOD}.get", triggerid=triggerid, **filters)
    
    def update(self, triggerid, **params):
        """
        Update existing triggers.
        
        Args:
            triggerid (str): ID of the trigger to update.
            
        Keyword Args (params):
            description (str, optional): Name of the trigger.
            expression (str, optional): Reduced trigger expression.
            event_name (str, optional): Event name generation method.
            opdata (str, optional): Operational data to display with trigger name.
            comments (str, optional): Trigger comments.
            priority (int, optional): Severity of the trigger (0-5).
            status (int, optional): Whether the trigger is enabled (0: enabled, 1: disabled).
            type (int, optional): Type of the trigger (0: normal, 1: multiple).
            recover_mode (int, optional): OK event generation mode.
            corr_mode (int, optional): Correlation mode.
            corr_conditionid (str, optional): ID of the correlation rule.
            manual_close (int, optional): Allow manual close (0: no, 1: yes).
            tags (list, optional): Trigger tags.
            dependencies (list, optional): Trigger dependencies.
        
        Returns:
            dict: API response containing the IDs of updated triggers.
        
        Example:
            >>> zapi.triggers.update(
            ...     triggerid="12345",
            ...     priority=5,
            ...     status=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/trigger/update
        """
        return self._call(f"{self.API_METHOD}.update", triggerid=triggerid, **params)