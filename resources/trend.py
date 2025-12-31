# resources/trend.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/trend

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TrendResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "trend"
    
    def get(self, **params):
        """
        Retrieve item trend data.
        
        Keyword Args (params):
            itemids (list, required): IDs of items to retrieve trends for.
            time_from (int, optional): Return only trend records from this timestamp.
            time_till (int, optional): Return only trend records until this timestamp.
            output (str, optional): Output format ("extend" or "count").
            sortfield (str, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing trend records.
        
        Example:
            >>> trends = zapi.trends.get(
            ...     itemids=["12345"],
            ...     time_from=timestamp,
            ...     time_till=timestamp_end,
            ...     limit=1000
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/trend/get
        """
        return self._call(f"{self.API_METHOD}.get", **params)