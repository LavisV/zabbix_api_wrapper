# resources/regular_expression.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/regexp

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class RegularExpressionResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "regexp"

    def create(self, **params):
        """
        Create new regular expressions.
        
        Keyword Args (params):
            name (str, required): Name of the regular expression.
            expressions (list, required): Regular expression entries. Each object should contain expression, expression_type, case_sensitive.
        
        Returns:
            dict: API response containing the IDs of created regular expressions.
        
        Example:
            >>> regexp = zapi.regular_expressions.create(
            ...     name="IP Address Pattern",
            ...     expressions=[{
            ...         "expression": "^([0-9]{1,3}\\.){3}[0-9]{1,3}$",
            ...         "expression_type": 0,
            ...         "case_sensitive": 0
            ...     }]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/regexp/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, regexpid):
        """
        Delete regular expressions.
        
        Args:
            regexpid (str|list): ID or list of IDs of regular expressions to delete.
        
        Returns:
            dict: API response containing the IDs of deleted regular expressions.
        
        Example:
            >>> # Delete a single regular expression
            >>> zapi.regular_expressions.delete(regexpid="1")
            >>> 
            >>> # Delete multiple regular expressions
            >>> zapi.regular_expressions.delete(regexpid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/regexp/delete
        """
        return self._call(f"{self.API_METHOD}.delete", regexpid=regexpid)

    def get(self, regexpid=None, **filters):
        """
        Retrieve regular expressions according to the given parameters.
        
        Args:
            regexpid (str|list, optional): Return only regular expressions with the given IDs.
            
        Keyword Args (filters):
            selectExpressions (str|list, optional): Include expressions in the result.
            filter (dict, optional): Filter regular expressions by given properties.
            search (dict, optional): Search regular expressions by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing regular expressions matching the criteria.
        
        Example:
            >>> # Get all regular expressions
            >>> regexps = zapi.regular_expressions.get()
            >>> 
            >>> # Get regular expression with expressions
            >>> regexp = zapi.regular_expressions.get(regexpid="1", selectExpressions="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/regexp/get
        """
        return self._call(f"{self.API_METHOD}.get", regexpid=regexpid, **filters)
    
    def update(self, regexpid, **params):
        """
        Update existing regular expressions.
        
        Args:
            regexpid (str): ID of the regular expression to update.
            
        Keyword Args (params):
            name (str, optional): Name of the regular expression.
            expressions (list, optional): Regular expression entries.
        
        Returns:
            dict: API response containing the IDs of updated regular expressions.
        
        Example:
            >>> zapi.regular_expressions.update(
            ...     regexpid="1",
            ...     name="Updated Pattern Name",
            ...     expressions=[...]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/regexp/update
        """
        return self._call(f"{self.API_METHOD}.update", regexpid=regexpid, **params)