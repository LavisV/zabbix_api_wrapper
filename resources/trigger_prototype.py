# resources/trigger_prototype.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/triggerprototype

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TriggerPrototypeResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "triggerprototype"

    def create(self, **params):
        """
        Create new trigger prototypes.
        
        Keyword Args (params):
            description (str, required): Name of the trigger prototype.
            expression (str, required): Reduced trigger expression.
            discovery_ruleid (str, required): ID of the LLD rule that the trigger prototype belongs to.
            event_name (str, optional): Event name generation method.
            opdata (str, optional): Operational data to display with trigger name.
            comments (str, optional): Trigger prototype comments.
            priority (int, optional): Severity of the trigger prototype (0-5).
            status (int, optional): Whether the trigger prototype is enabled (0: enabled, 1: disabled).
            type (int, optional): Type of the trigger prototype (0: normal, 1: multiple).
            recover_mode (int, optional): OK event generation mode.
            corr_mode (int, optional): Correlation mode.
            corr_conditionid (str, optional): ID of the correlation rule.
            manual_close (int, optional): Allow manual close (0: no, 1: yes).
            tags (list, optional): Trigger prototype tags.
            dependencies (list, optional): Trigger prototype dependencies. Each object should have a triggerid.
        
        Returns:
            dict: API response containing the IDs of created trigger prototypes.
        
        Example:
            >>> trigger_prototype = zapi.trigger_prototypes.create(
            ...     description="High CPU usage on {#CPU.NUMBER}",
            ...     expression="{host:system.cpu.util[{#CPU.NUMBER}].avg(5m)}>80",
            ...     discovery_ruleid="1",
            ...     priority=3
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/triggerprototype/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, triggerprototypeid):
        """
        Delete trigger prototypes.
        
        Args:
            triggerprototypeid (str|list): ID or list of IDs of trigger prototypes to delete.
        
        Returns:
            dict: API response containing the IDs of deleted trigger prototypes.
        
        Example:
            >>> # Delete a single trigger prototype
            >>> zapi.trigger_prototypes.delete(triggerprototypeid="1")
            >>> 
            >>> # Delete multiple trigger prototypes
            >>> zapi.trigger_prototypes.delete(triggerprototypeid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/triggerprototype/delete
        """
        return self._call(f"{self.API_METHOD}.delete", triggerprototypeid=triggerprototypeid)

    def get(self, triggerprototypeid=None, **filters):
        """
        Retrieve trigger prototypes according to the given parameters.
        
        Args:
            triggerprototypeid (str|list, optional): Return only trigger prototypes with the given IDs.
            
        Keyword Args (filters):
            discoveryids (list, optional): Return only trigger prototypes that belong to the given LLD rules.
            itemids (list, optional): Return only trigger prototypes that use the given item prototypes.
            functions (list, optional): Return only trigger prototypes that use the given functions.
            inherited (bool, optional): Return only inherited trigger prototypes.
            templated (bool, optional): Return only trigger prototypes that belong to templates.
            monitored (bool, optional): Return only enabled trigger prototypes that belong to monitored hosts.
            active (bool, optional): Return only enabled trigger prototypes.
            maintenance (bool, optional): Return only trigger prototypes in maintenance state.
            min_severity (int, optional): Return only trigger prototypes with severity greater than or equal to this value.
            evaltype (int, optional): Rules for tag evaluation.
            tags (list, optional): Return only trigger prototypes with given tags.
            expandDescription (bool, optional): Expand macros in trigger prototype description.
            expandComment (bool, optional): Expand macros in trigger prototype comments.
            expandExpression (bool, optional): Expand macros in trigger prototype expression.
            selectHosts (str|list, optional): Include hosts in the result.
            selectItems (str|list, optional): Include item prototypes in the result.
            selectFunctions (str|list, optional): Include functions in the result.
            selectDependencies (str|list, optional): Include dependencies in the result.
            selectDiscoveryRule (str|list, optional): Include LLD rule in the result.
            selectTags (str|list, optional): Include tags in the result.
            filter (dict, optional): Filter trigger prototypes by given properties.
            search (dict, optional): Search trigger prototypes by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing trigger prototypes matching the criteria.
        
        Example:
            >>> # Get all trigger prototypes
            >>> trigger_prototypes = zapi.trigger_prototypes.get()
            >>> 
            >>> # Get trigger prototypes for an LLD rule
            >>> trigger_prototypes = zapi.trigger_prototypes.get(discoveryids=["1"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/triggerprototype/get
        """
        return self._call(f"{self.API_METHOD}.get", triggerprototypeid=triggerprototypeid, **filters)
    
    def update(self, triggerprototypeid, **params):
        """
        Update existing trigger prototypes.
        
        Args:
            triggerprototypeid (str): ID of the trigger prototype to update.
            
        Keyword Args (params):
            description (str, optional): Name of the trigger prototype.
            expression (str, optional): Reduced trigger expression.
            discovery_ruleid (str, optional): ID of the LLD rule that the trigger prototype belongs to.
            event_name (str, optional): Event name generation method.
            opdata (str, optional): Operational data to display with trigger name.
            comments (str, optional): Trigger prototype comments.
            priority (int, optional): Severity of the trigger prototype (0-5).
            status (int, optional): Whether the trigger prototype is enabled (0: enabled, 1: disabled).
            type (int, optional): Type of the trigger prototype (0: normal, 1: multiple).
            recover_mode (int, optional): OK event generation mode.
            corr_mode (int, optional): Correlation mode.
            corr_conditionid (str, optional): ID of the correlation rule.
            manual_close (int, optional): Allow manual close (0: no, 1: yes).
            tags (list, optional): Trigger prototype tags.
            dependencies (list, optional): Trigger prototype dependencies.
        
        Returns:
            dict: API response containing the IDs of updated trigger prototypes.
        
        Example:
            >>> zapi.trigger_prototypes.update(
            ...     triggerprototypeid="1",
            ...     priority=5,
            ...     status=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/triggerprototype/update
        """
        return self._call(f"{self.API_METHOD}.update", triggerprototypeid=triggerprototypeid, **params)