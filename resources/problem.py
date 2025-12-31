# resources/problem.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/problem

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ProblemResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "problem"

    def get(self, **params):
        """
        Retrieve problems according to the given parameters.
        
        Keyword Args (params):
            eventids (list, optional): Return only problems with the given event IDs.
            groupids (list, optional): Return only problems that belong to the given host groups.
            hostids (list, optional): Return only problems that belong to the given hosts.
            objectids (list, optional): Return only problems that belong to the given objects.
            source (int, optional): Return only problems with the given event source.
            object (int, optional): Return only problems created by the given object type.
            acknowledged (bool, optional): Return only acknowledged or unacknowledged problems.
            suppressed (bool, optional): Return only suppressed or unsuppressed problems.
            severities (list, optional): Return only problems with the given severities.
            evaltype (int, optional): Rules for tag evaluation.
            tags (list, optional): Return only problems with given tags.
            time_from (int, optional): Return only problems that have been created after or at the given time.
            time_till (int, optional): Return only problems that have been created before or at the given time.
            recent (bool, optional): Return only recent problems.
            eventid_from (str, optional): Return only problems with event ID greater or equal to the given ID.
            eventid_till (str, optional): Return only problems with event ID less or equal to the given ID.
            selectAcknowledges (str|list, optional): Include acknowledges in the result.
            selectTags (str|list, optional): Include tags in the result.
            selectSuppressionData (str|bool, optional): Include suppression data in the result.
            filter (dict, optional): Filter problems by given properties.
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing problems matching the criteria.
        
        Example:
            >>> # Get all problems
            >>> problems = zapi.problems.get()
            >>> 
            >>> # Get unacknowledged problems
            >>> problems = zapi.problems.get(acknowledged=False)
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/problem/get
        """
        return self._call(f"{self.API_METHOD}.get", **params)