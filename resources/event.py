# resources/event.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/event

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class EventResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "event"

    def get(self, **filters):
        """
        Retrieve events according to the given parameters.
        
        Keyword Args (filters):
            eventids (list, optional): Return only events with the given IDs.
            groupids (list, optional): Return only events created by objects that belong to the given host groups.
            hostids (list, optional): Return only events created by objects that belong to the given hosts.
            objectids (list, optional): Return only events created by the given objects.
            source (int, optional): Return only events with the given event source (0: trigger, 1: discovery, 2: autoregistration, 3: internal).
            object (int, optional): Return only events created by the given object type (0: trigger, 4: item, 5: LLD rule).
            acknowledged (bool, optional): Return only acknowledged or unacknowledged events.
            suppressed (bool, optional): Return only suppressed or unsuppressed events.
            severities (list, optional): Return only events with the given severities.
            evaltype (int, optional): Rules for tag evaluation.
            tags (list, optional): Return only events with given tags.
            time_from (int, optional): Return only events that have been created after or at the given time.
            time_till (int, optional): Return only events that have been created before or at the given time.
            eventid_from (str, optional): Return only events with ID greater or equal to the given ID.
            eventid_till (str, optional): Return only events with ID less or equal to the given ID.
            value (list, optional): Return only events with the given values (0: OK, 1: problem).
            selectHosts (str|list, optional): Include hosts in the result.
            selectRelatedObject (str|list, optional): Include related object in the result.
            selectAlerts (str|list, optional): Include alerts in the result.
            selectAcknowledges (str|list, optional): Include acknowledges in the result.
            selectTags (str|list, optional): Include tags in the result.
            selectSuppressionData (str|bool, optional): Include suppression data in the result.
            filter (dict, optional): Filter events by given properties.
            search (dict, optional): Search events by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing events matching the criteria.
        
        Example:
            >>> # Get recent events
            >>> events = zapi.events.get(time_from=timestamp)
            >>> 
            >>> # Get unacknowledged events
            >>> events = zapi.events.get(acknowledged=False)
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/event/get
        """
        return self._call(f"{self.API_METHOD}.get", **filters)
    
    def acknowledge(self, **params):
        """
        Acknowledge events.
        
        Keyword Args (params):
            eventids (list, required): IDs of events to acknowledge.
            action (int, optional): Acknowledge operation action (1: close problem, 2: acknowledge, 4: add message, 8: change severity, 16: change unacknowledged).
            message (str, optional): Acknowledge message.
            severity (int, optional): New severity level (0-5).
        
        Returns:
            dict: API response containing event IDs that were acknowledged.
        
        Example:
            >>> zapi.events.acknowledge(
            ...     eventids=["12345"],
            ...     action=2,
            ...     message="Acknowledged by operator"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/event/acknowledge
        """
        return self._call(f"{self.API_METHOD}.acknowledge", **params)