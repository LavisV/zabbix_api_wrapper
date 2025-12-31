# resources/correlation.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/correlation

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class CorrelationResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "correlation"

    def create(self, **params):
        """
        Create new event correlation rules.
        
        Keyword Args (params):
            name (str, required): Name of the correlation rule.
            status (int, optional): Whether the correlation rule is enabled (0: enabled, 1: disabled).
            evaltype (int, required): Evaluation method (0: formula or custom expression, 1: conditions).
            formula (str, optional): Custom correlation formula (required if evaltype is 0).
            conditions (list, required): Correlation conditions (required if evaltype is 1). Each object should contain type, tag, oldtag, newtag, opgroup, opstatus, optag, operator, value.
            operations (list, optional): Operations to perform when conditions are met.
            description (str, optional): Description of the correlation rule.
        
        Returns:
            dict: API response containing the IDs of created correlation rules.
        
        Example:
            >>> correlation = zapi.correlations.create(
            ...     name="Auto Close Correlated Events",
            ...     status=0,
            ...     evaltype=1,
            ...     conditions=[...],
            ...     operations=[...]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/correlation/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, correlationid):
        """
        Delete event correlation rules.
        
        Args:
            correlationid (str|list): ID or list of IDs of correlation rules to delete.
        
        Returns:
            dict: API response containing the IDs of deleted correlation rules.
        
        Example:
            >>> # Delete a single correlation rule
            >>> zapi.correlations.delete(correlationid="1")
            >>> 
            >>> # Delete multiple correlation rules
            >>> zapi.correlations.delete(correlationid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/correlation/delete
        """
        return self._call(f"{self.API_METHOD}.delete", correlationid=correlationid)

    def get(self, correlationid=None, **filters):
        """
        Retrieve event correlation rules according to the given parameters.
        
        Args:
            correlationid (str|list, optional): Return only correlation rules with the given IDs.
            
        Keyword Args (filters):
            selectOperations (str|list, optional): Include operations in the result.
            selectFilter (str|list, optional): Include filter in the result.
            filter (dict, optional): Filter correlation rules by given properties.
            search (dict, optional): Search correlation rules by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing correlation rules matching the criteria.
        
        Example:
            >>> # Get all correlation rules
            >>> correlations = zapi.correlations.get()
            >>> 
            >>> # Get correlation rule with operations
            >>> correlation = zapi.correlations.get(correlationid="1", selectOperations="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/correlation/get
        """
        return self._call(f"{self.API_METHOD}.get", correlationid=correlationid, **filters)
    
    def update(self, correlationid, **params):
        """
        Update existing event correlation rules.
        
        Args:
            correlationid (str): ID of the correlation rule to update.
            
        Keyword Args (params):
            name (str, optional): Name of the correlation rule.
            status (int, optional): Whether the correlation rule is enabled (0: enabled, 1: disabled).
            evaltype (int, optional): Evaluation method.
            formula (str, optional): Custom correlation formula.
            conditions (list, optional): Correlation conditions.
            operations (list, optional): Operations to perform when conditions are met.
            description (str, optional): Description of the correlation rule.
        
        Returns:
            dict: API response containing the IDs of updated correlation rules.
        
        Example:
            >>> zapi.correlations.update(
            ...     correlationid="1",
            ...     name="Updated Correlation Rule Name",
            ...     status=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/correlation/update
        """
        return self._call(f"{self.API_METHOD}.update", correlationid=correlationid, **params)