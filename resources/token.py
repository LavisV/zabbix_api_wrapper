# resources/token.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/token

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TokenResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "token"

    def create(self, **params):
        """
        Create new API tokens.
        
        Keyword Args (params):
            name (str, required): Name of the token.
            userid (str, required): ID of the user to create the token for.
            description (str, optional): Description of the token.
            expires_at (int, optional): Token expiration time (Unix timestamp, 0: no expiration).
            status (int, optional): Whether the token is enabled (0: enabled, 1: disabled).
        
        Returns:
            dict: API response containing the IDs of created tokens.
        
        Example:
            >>> token = zapi.tokens.create(
            ...     name="API Token",
            ...     userid="1",
            ...     expires_at=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/token/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, tokenid):
        """
        Delete API tokens.
        
        Args:
            tokenid (str|list): ID or list of IDs of tokens to delete.
        
        Returns:
            dict: API response containing the IDs of deleted tokens.
        
        Example:
            >>> # Delete a single token
            >>> zapi.tokens.delete(tokenid="1")
            >>> 
            >>> # Delete multiple tokens
            >>> zapi.tokens.delete(tokenid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/token/delete
        """
        return self._call(f"{self.API_METHOD}.delete", tokenid=tokenid)

    def generate(self, **params):
        """
        Generate a new API token.
        
        Keyword Args (params):
            name (str, required): Name of the token.
            userid (str, required): ID of the user to create the token for.
            auth_token (str, optional): Authentication token string (if not provided, will be generated).
            expires_at (int, optional): Token expiration time (Unix timestamp, 0: no expiration).
            description (str, optional): Description of the token.
        
        Returns:
            dict: API response containing the generated token information including the auth_token.
        
        Example:
            >>> token = zapi.tokens.generate(
            ...     name="New API Token",
            ...     userid="1"
            ... )
            >>> auth_token = token["result"]["auth_token"]
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/token/generate
        """
        return self._call(f"{self.API_METHOD}.generate", **params)

    def get(self, tokenid=None, **filters):
        """
        Retrieve API tokens according to the given parameters.
        
        Args:
            tokenid (str|list, optional): Return only tokens with the given IDs.
            
        Keyword Args (filters):
            userids (list, optional): Return only tokens that belong to the given users.
            filter (dict, optional): Filter tokens by given properties.
            search (dict, optional): Search tokens by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing tokens matching the criteria.
        
        Example:
            >>> # Get all tokens
            >>> tokens = zapi.tokens.get()
            >>> 
            >>> # Get tokens for a user
            >>> tokens = zapi.tokens.get(userids=["1"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/token/get
        """
        return self._call(f"{self.API_METHOD}.get", tokenid=tokenid, **filters)
      
    def update(self, tokenid, **params):
        """
        Update existing API tokens.
        
        Args:
            tokenid (str): ID of the token to update.
            
        Keyword Args (params):
            name (str, optional): Name of the token.
            description (str, optional): Description of the token.
            expires_at (int, optional): Token expiration time (Unix timestamp, 0: no expiration).
            status (int, optional): Whether the token is enabled (0: enabled, 1: disabled).
        
        Returns:
            dict: API response containing the IDs of updated tokens.
        
        Example:
            >>> zapi.tokens.update(
            ...     tokenid="1",
            ...     name="Updated Token Name",
            ...     status=1
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/token/update
        """
        return self._call(f"{self.API_METHOD}.update", tokenid=tokenid, **params)