# resources/module.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/module

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ModuleResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "module"

    def create(self, **params):
        """
        Create new modules.
        
        Keyword Args (params):
            id (str, required): Module identifier.
            relative_path (str, required): Relative path to the module file.
            status (int, optional): Module status (0: enabled, 1: disabled).
            config (dict, optional): Module configuration.
        
        Returns:
            dict: API response containing the IDs of created modules.
        
        Example:
            >>> module = zapi.modules.create(
            ...     id="example_module",
            ...     relative_path="modules/example.so",
            ...     status=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/module/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)

    def delete(self, moduleid):
        """
        Delete modules.
        
        Args:
            moduleid (str|list): ID or list of IDs of modules to delete.
        
        Returns:
            dict: API response containing the IDs of deleted modules.
        
        Example:
            >>> # Delete a single module
            >>> zapi.modules.delete(moduleid="example_module")
            >>> 
            >>> # Delete multiple modules
            >>> zapi.modules.delete(moduleid=["module1", "module2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/module/delete
        """
        return self._call(f"{self.API_METHOD}.delete", moduleid=moduleid)
    
    def get(self, moduleid=None, **filters):
        """
        Retrieve modules according to the given parameters.
        
        Args:
            moduleid (str|list, optional): Return only modules with the given IDs.
            
        Keyword Args (filters):
            filter (dict, optional): Filter modules by given properties.
            search (dict, optional): Search modules by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing modules matching the criteria.
        
        Example:
            >>> # Get all modules
            >>> modules = zapi.modules.get()
            >>> 
            >>> # Get module by ID
            >>> module = zapi.modules.get(moduleid="example_module")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/module/get
        """
        return self._call(f"{self.API_METHOD}.get", moduleid=moduleid, **filters)
    
    def update(self, moduleid, **params):
        """
        Update existing modules.
        
        Args:
            moduleid (str): ID of the module to update.
            
        Keyword Args (params):
            relative_path (str, optional): Relative path to the module file.
            status (int, optional): Module status (0: enabled, 1: disabled).
            config (dict, optional): Module configuration.
        
        Returns:
            dict: API response containing the IDs of updated modules.
        
        Example:
            >>> zapi.modules.update(
            ...     moduleid="example_module",
            ...     status=1
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/module/update
        """
        return self._call(f"{self.API_METHOD}.update", moduleid=moduleid, **params)