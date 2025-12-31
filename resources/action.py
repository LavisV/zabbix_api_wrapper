# resources/action.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/action

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ActionResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)
    
    API_METHOD = "action"

    def create(self, **params):
        """
        Create new actions.
        
        Keyword Args (params):
            name (str, required): Name of the action.
            eventsource (int, required): Type of events that the action handles (0: event created by trigger, 1: event created by discovery rule, 2: event created by active agent autoregistration, 3: event created by internal event source).
            status (int, optional): Whether the action is enabled (0: enabled, 1: disabled).
            esc_period (str, optional): Action operation escalation time period.
            def_shortdata (str, optional): Default operation message subject.
            def_longdata (str, optional): Default operation message text.
            r_shortdata (str, optional): Recovery operation message subject.
            r_longdata (str, optional): Recovery operation message text.
            ack_shortdata (str, optional): Acknowledge operation message subject.
            ack_longdata (str, optional): Acknowledge operation message text.
            formula (str, optional): Action condition evaluation formula.
            evaltype (int, optional): Action condition evaluation method (0: AND/OR, 1: AND, 2: OR).
            conditions (list, required): Action conditions.
            operations (list, required): Action operations to perform.
            recovery_operations (list, optional): Recovery operations to perform.
            acknowledge_operations (list, optional): Acknowledge operations to perform.
            filter (dict, optional): Filter properties.
        
        Returns:
            dict: API response containing the IDs of created actions.
        
        Example:
            >>> action = zapi.actions.create(
            ...     name="Send Email on Problem",
            ...     eventsource=0,
            ...     conditions=[...],
            ...     operations=[...]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/action/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, actionid):
        """
        Delete actions.
        
        Args:
            actionid (str|list): ID or list of IDs of actions to delete.
        
        Returns:
            dict: API response containing the IDs of deleted actions.
        
        Example:
            >>> # Delete a single action
            >>> zapi.actions.delete(actionid="1")
            >>> 
            >>> # Delete multiple actions
            >>> zapi.actions.delete(actionid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/action/delete
        """
        return self._call(f"{self.API_METHOD}.delete", actionids=[actionid])

    def get(self, **filters):
        """
        Retrieve actions according to the given parameters.
        
        Keyword Args (filters):
            actionids (list, optional): Return only actions with the given IDs.
            groupids (list, optional): Return only actions that belong to the given host groups.
            hostids (list, optional): Return only actions that belong to the given hosts.
            triggerids (list, optional): Return only actions that use the given triggers.
            mediatypeids (list, optional): Return only actions that use the given media types.
            usrgrpids (list, optional): Return only actions that send messages to the given user groups.
            userids (list, optional): Return only actions that send messages to the given users.
            scriptids (list, optional): Return only actions that execute the given scripts.
            selectOperations (str|list, optional): Include operations in the result.
            selectRecoveryOperations (str|list, optional): Include recovery operations in the result.
            selectAcknowledgeOperations (str|list, optional): Include acknowledge operations in the result.
            selectFilter (str|list, optional): Include filter in the result.
            filter (dict, optional): Filter actions by given properties.
            search (dict, optional): Search actions by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing actions matching the criteria.
        
        Example:
            >>> # Get all actions
            >>> actions = zapi.actions.get()
            >>> 
            >>> # Get actions with operations
            >>> actions = zapi.actions.get(selectOperations="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/action/get
        """
        return self._call(f"{self.API_METHOD}.get", **filters)
    
    def massadd(self, **params):
        """
        Mass add related objects to actions.
        
        Keyword Args (params):
            actionids (list, required): IDs of actions to update.
            operations (list, optional): Operations to add to the actions.
            recovery_operations (list, optional): Recovery operations to add to the actions.
            acknowledge_operations (list, optional): Acknowledge operations to add to the actions.
        
        Returns:
            dict: API response containing the IDs of updated actions.
        
        Example:
            >>> zapi.actions.massadd(
            ...     actionids=["1", "2"],
            ...     operations=[...]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/action/massadd
        """
        return self._call(f"{self.API_METHOD}.massadd", **params)