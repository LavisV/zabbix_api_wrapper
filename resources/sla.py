# resources/sla.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/sla

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class SLAResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "sla"

    def create(self, **params):
        """
        Create new SLA objects.
        
        Keyword Args (params):
            name (str, required): Name of the SLA.
            period (int, required): SLA period in seconds.
            slo (float, required): Service level objective (SLO) in percentage (0-100).
            effective_date (int, required): SLA effective date (Unix timestamp).
            timezone (str, optional): SLA timezone.
            status (int, optional): Whether the SLA is enabled (0: enabled, 1: disabled).
            description (str, optional): Description of the SLA.
            tags (list, optional): SLA tags.
            serviceids (list, optional): Service IDs to apply the SLA to.
            excluded_downtimes (list, optional): Excluded downtime periods.
            schedule (list, optional): SLA schedule.
        
        Returns:
            dict: API response containing the IDs of created SLAs.
        
        Example:
            >>> sla = zapi.slas.create(
            ...     name="99.9% Uptime SLA",
            ...     period=31536000,
            ...     slo=99.9,
            ...     effective_date=timestamp
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/sla/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, slaid):
        """
        Delete SLA objects.
        
        Args:
            slaid (str|list): ID or list of IDs of SLAs to delete.
        
        Returns:
            dict: API response containing the IDs of deleted SLAs.
        
        Example:
            >>> # Delete a single SLA
            >>> zapi.slas.delete(slaid="1")
            >>> 
            >>> # Delete multiple SLAs
            >>> zapi.slas.delete(slaid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/sla/delete
        """
        return self._call(f"{self.API_METHOD}.delete", slaid=slaid)

    def get(self, slaid=None, **filters):
        """
        Retrieve SLA objects according to the given parameters.
        
        Args:
            slaid (str|list, optional): Return only SLAs with the given IDs.
            
        Keyword Args (filters):
            serviceids (list, optional): Return only SLAs that apply to the given services.
            selectServiceids (str|list, optional): Include service IDs in the result.
            selectExcludedDowntimes (str|list, optional): Include excluded downtimes in the result.
            selectSchedule (str|list, optional): Include schedule in the result.
            filter (dict, optional): Filter SLAs by given properties.
            search (dict, optional): Search SLAs by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing SLAs matching the criteria.
        
        Example:
            >>> # Get all SLAs
            >>> slas = zapi.slas.get()
            >>> 
            >>> # Get SLA by ID
            >>> sla = zapi.slas.get(slaid="1")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/sla/get
        """
        return self._call(f"{self.API_METHOD}.get", slaid=slaid, **filters)

    def get_sli(self, **params):
        """
        Retrieve Service Level Indicator (SLI) data.
        
        Keyword Args (params):
            slaid (str, required): SLA ID.
            period_from (int, required): Start time of the period (Unix timestamp).
            period_to (int, required): End time of the period (Unix timestamp).
            periods (int, optional): Number of periods to retrieve.
            periods_count (int, optional): Number of periods for calculation.
            serviceids (list, optional): Service IDs to calculate SLI for.
        
        Returns:
            dict: API response containing SLI data.
        
        Example:
            >>> sli = zapi.slas.get_sli(
            ...     slaid="1",
            ...     period_from=timestamp_start,
            ...     period_to=timestamp_end
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/sla/getsli
        """
        return self._call(f"{self.API_METHOD}.getsli", **params)
