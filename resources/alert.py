# resources/alert.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/alert

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class AlertResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "alert"

    def get(self, alertid=None, **filters):
        """
        Retrieve alerts according to the given parameters.
        
        Args:
            alertid (str|list, optional): Return only alerts with the given IDs.
            
        Keyword Args (filters):
            actionids (list, optional): Return only alerts triggered by the given actions.
            eventids (list, optional): Return only alerts triggered by the given events.
            groupids (list, optional): Return only alerts that belong to the given host groups.
            hostids (list, optional): Return only alerts that belong to the given hosts.
            mediatypeids (list, optional): Return only alerts sent via the given media types.
            objectids (list, optional): Return only alerts triggered by the given objects.
            userids (list, optional): Return only alerts sent to the given users.
            clock_from (int, optional): Return only alerts created after or at the given time.
            clock_to (int, optional): Return only alerts created before or at the given time.
            eventvalue (list, optional): Return only alerts with the given event values.
            selectHosts (str|list, optional): Include hosts in the result.
            selectMediatypes (str|list, optional): Include media types in the result.
            filter (dict, optional): Filter alerts by given properties.
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing alerts matching the criteria.
        
        Example:
            >>> # Get all alerts
            >>> alerts = zapi.alerts.get()
            >>> 
            >>> # Get alerts for an event
            >>> alerts = zapi.alerts.get(eventids=["12345"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/alert/get
        """
        return self._call(f"{self.API_METHOD}.get", alertid=alertid, **filters)