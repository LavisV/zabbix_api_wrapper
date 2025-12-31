# resources/auditlog.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/auditlog

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class AuditLogResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "auditlog"

    def get(self, **filters):
        """
        Retrieve audit log records according to the given parameters.
        
        Keyword Args (filters):
            recordsetid (str, optional): Return only audit log records with the given recordset ID.
            auditids (list, optional): Return only audit log records with the given IDs.
            userids (list, optional): Return only audit log records created by the given users.
            time_from (int, optional): Return only audit log records created after or at the given time.
            time_till (int, optional): Return only audit log records created before or at the given time.
            filter (dict, optional): Filter audit log records by given properties.
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing audit log records matching the criteria.
        
        Example:
            >>> # Get all audit log records
            >>> audit_logs = zapi.auditlog.get()
            >>> 
            >>> # Get audit logs for a time period
            >>> audit_logs = zapi.auditlog.get(time_from=timestamp, time_till=timestamp_end)
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/auditlog/get
        """
        return self._call(f"{self.API_METHOD}.get", **filters)