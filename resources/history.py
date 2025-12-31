# resources/history.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/history

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HistoryResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "history"

    def clear(self, **params):
        """
        Clear item history.
        
        Keyword Args (params):
            itemids (list, optional): IDs of items to clear history for.
            history (int, optional): History type to clear (0: float, 1: string, 2: log, 3: unsigned integer, 4: text).
            time_from (int, optional): Clear history from this timestamp.
            time_till (int, optional): Clear history until this timestamp.
        
        Returns:
            dict: API response containing the number of deleted records.
        
        Example:
            >>> zapi.history.clear(
            ...     itemids=["12345"],
            ...     history=0,
            ...     time_from=timestamp
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/history/clear
        """
        return self._call(f"{self.API_METHOD}.clear", **params)

    def get(self, **params):
        """
        Retrieve item history data.
        
        Keyword Args (params):
            itemids (list, required): IDs of items to retrieve history for.
            history (int, required): History type to retrieve (0: float, 1: string, 2: log, 3: unsigned integer, 4: text).
            time_from (int, optional): Return only history records from this timestamp.
            time_till (int, optional): Return only history records until this timestamp.
            output (str, optional): Output format ("extend" or "count").
            sortfield (str, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing history records.
        
        Example:
            >>> history = zapi.history.get(
            ...     itemids=["12345"],
            ...     history=0,
            ...     time_from=timestamp,
            ...     limit=100
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/history/get
        """
        return self._call(f"{self.API_METHOD}.get", **params)

    def push(self, **params):
        """
        Push item history data.
        
        Keyword Args (params):
            history (list, required): History records to push. Each object should contain itemid, clock, ns, value, value_type.
        
        Returns:
            dict: API response containing the number of pushed records.
        
        Example:
            >>> zapi.history.push(
            ...     history=[{
            ...         "itemid": "12345",
            ...         "clock": timestamp,
            ...         "ns": 0,
            ...         "value": "42.5",
            ...         "value_type": 0
            ...     }]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/history/push
        """
        return self._call(f"{self.API_METHOD}.push", **params)