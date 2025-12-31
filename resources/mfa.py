# resources/mfa.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/mfa

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class MFAResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "mfa"

    def create(self, **params):
        """
        Create new MFA (Multi-Factor Authentication) methods.
        
        Keyword Args (params):
            name (str, required): Name of the MFA method.
            mfaid (str, required): MFA method identifier.
            hash_function (str, required): Hash function for TOTP.
            code_length (int, required): Code length for TOTP.
            issuer (str, optional): Issuer name.
            digits (int, optional): Number of digits in the code.
            algorithm (str, optional): Algorithm for TOTP (SHA1, SHA256, SHA512).
            period (int, optional): Time period for TOTP in seconds.
        
        Returns:
            dict: API response containing the IDs of created MFA methods.
        
        Example:
            >>> mfa = zapi.mfa.create(
            ...     name="TOTP",
            ...     mfaid="totp",
            ...     hash_function="SHA1",
            ...     code_length=6
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/mfa/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, mfaid):
        """
        Delete MFA methods.
        
        Args:
            mfaid (str|list): ID or list of IDs of MFA methods to delete.
        
        Returns:
            dict: API response containing the IDs of deleted MFA methods.
        
        Example:
            >>> # Delete a single MFA method
            >>> zapi.mfa.delete(mfaid="totp")
            >>> 
            >>> # Delete multiple MFA methods
            >>> zapi.mfa.delete(mfaid=["totp", "duo"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/mfa/delete
        """
        return self._call(f"{self.API_METHOD}.delete", mfaid=mfaid)

    def get(self, mfaid=None, **filters):
        """
        Retrieve MFA methods according to the given parameters.
        
        Args:
            mfaid (str|list, optional): Return only MFA methods with the given IDs.
            
        Keyword Args (filters):
            filter (dict, optional): Filter MFA methods by given properties.
            search (dict, optional): Search MFA methods by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing MFA methods matching the criteria.
        
        Example:
            >>> # Get all MFA methods
            >>> mfa_methods = zapi.mfa.get()
            >>> 
            >>> # Get MFA method by ID
            >>> mfa = zapi.mfa.get(mfaid="totp")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/mfa/get
        """
        return self._call(f"{self.API_METHOD}.get", mfaid=mfaid, **filters)
    
    def update(self, mfaid, **params):
        """
        Update existing MFA methods.
        
        Args:
            mfaid (str): ID of the MFA method to update.
            
        Keyword Args (params):
            name (str, optional): Name of the MFA method.
            hash_function (str, optional): Hash function for TOTP.
            code_length (int, optional): Code length for TOTP.
            issuer (str, optional): Issuer name.
            digits (int, optional): Number of digits in the code.
            algorithm (str, optional): Algorithm for TOTP.
            period (int, optional): Time period for TOTP in seconds.
        
        Returns:
            dict: API response containing the IDs of updated MFA methods.
        
        Example:
            >>> zapi.mfa.update(
            ...     mfaid="totp",
            ...     name="Updated TOTP",
            ...     code_length=8
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/mfa/update
        """
        return self._call(f"{self.API_METHOD}.update", mfaid=mfaid, **params)