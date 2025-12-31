# resources/user_macro.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/usermacro

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class UserMacroResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "usermacro"

    def create(self, **params):
        """
        Create new user macros (host or template level).
        
        Keyword Args (params):
            macro (str, required): Macro name (e.g., "{$MACRO}").
            hostid (str, optional): ID of the host to create the macro for.
            templateid (str, optional): ID of the template to create the macro for.
            value (str, optional): Macro value.
            description (str, optional): Description of the macro.
            type (int, optional): Macro type (0: text macro, 1: secret macro).
        
        Returns:
            dict: API response containing the IDs of created user macros.
        
        Example:
            >>> macro = zapi.user_macros.create(
            ...     macro="{$SNMP_COMMUNITY}",
            ...     hostid="10105",
            ...     value="public"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/usermacro/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)

    def create_global(self, **params):
        """
        Create new global user macros.
        
        Keyword Args (params):
            macro (str, required): Macro name (e.g., "{$MACRO}").
            value (str, optional): Macro value.
            description (str, optional): Description of the macro.
            type (int, optional): Macro type (0: text macro, 1: secret macro).
        
        Returns:
            dict: API response containing the IDs of created global user macros.
        
        Example:
            >>> global_macro = zapi.user_macros.create_global(
            ...     macro="{$GLOBAL_MACRO}",
            ...     value="global_value"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/usermacro/createglobal
        """
        return self._call(f"{self.API_METHOD}.createglobal", **params)
    
    def delete(self, usermacroid):
        """
        Delete user macros (host or template level).
        
        Args:
            usermacroid (str|list): ID or list of IDs of user macros to delete.
        
        Returns:
            dict: API response containing the IDs of deleted user macros.
        
        Example:
            >>> # Delete a single user macro
            >>> zapi.user_macros.delete(usermacroid="1")
            >>> 
            >>> # Delete multiple user macros
            >>> zapi.user_macros.delete(usermacroid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/usermacro/delete
        """
        return self._call(f"{self.API_METHOD}.delete", usermacroid=usermacroid)

    def delete_global(self, **params):
        """
        Delete global user macros.
        
        Keyword Args (params):
            macro (str, required): Macro name to delete (e.g., "{$MACRO}").
        
        Returns:
            dict: API response containing the IDs of deleted global user macros.
        
        Example:
            >>> zapi.user_macros.delete_global(macro="{$GLOBAL_MACRO}")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/usermacro/deleteglobal
        """
        return self._call(f"{self.API_METHOD}.deleteglobal", **params)
    
    def get(self, **params):
        """
        Retrieve user macros according to the given parameters.
        
        Keyword Args (params):
            globalmacro (bool, optional): Return only global macros (true) or host/template macros (false).
            hostids (list, optional): Return only macros that belong to the given hosts.
            hostmacroids (list, optional): Return only macros with the given IDs (for host/template macros).
            globalmacroids (list, optional): Return only global macros with the given IDs.
            templateids (list, optional): Return only macros that belong to the given templates.
            selectHosts (str|list, optional): Include hosts in the result.
            selectTemplates (str|list, optional): Include templates in the result.
            filter (dict, optional): Filter user macros by given properties.
            search (dict, optional): Search user macros by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing user macros matching the criteria.
        
        Example:
            >>> # Get all user macros
            >>> macros = zapi.user_macros.get()
            >>> 
            >>> # Get global macros only
            >>> global_macros = zapi.user_macros.get(globalmacro=True)
            >>> 
            >>> # Get macros for a host
            >>> host_macros = zapi.user_macros.get(hostids=["10105"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/usermacro/get
        """
        return self._call(f"{self.API_METHOD}.get", **params)
    
    def update(self, **params):
        """
        Update existing user macros (host or template level).
        
        Keyword Args (params):
            hostmacroid (str, required): ID of the user macro to update.
            macro (str, optional): Macro name (e.g., "{$MACRO}").
            value (str, optional): Macro value.
            description (str, optional): Description of the macro.
            type (int, optional): Macro type (0: text macro, 1: secret macro).
        
        Returns:
            dict: API response containing the IDs of updated user macros.
        
        Example:
            >>> zapi.user_macros.update(
            ...     hostmacroid="1",
            ...     value="updated_value"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/usermacro/update
        """
        return self._call(f"{self.API_METHOD}.update", **params)
    
    def update_global(self, **params):
        """
        Update existing global user macros.
        
        Keyword Args (params):
            globalmacroid (str, required): ID of the global user macro to update.
            macro (str, optional): Macro name (e.g., "{$MACRO}").
            value (str, optional): Macro value.
            description (str, optional): Description of the macro.
            type (int, optional): Macro type (0: text macro, 1: secret macro).
        
        Returns:
            dict: API response containing the IDs of updated global user macros.
        
        Example:
            >>> zapi.user_macros.update_global(
            ...     globalmacroid="1",
            ...     value="updated_global_value"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/usermacro/updateglobal
        """
        return self._call(f"{self.API_METHOD}.updateglobal", **params)