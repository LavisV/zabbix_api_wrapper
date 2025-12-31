# resources/role.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/role

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class RoleResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "role"

    def create(self, **params):
        """
        Create new roles.
        
        Keyword Args (params):
            name (str, required): Name of the role.
            type (int, required): Type of the role (1: user role, 2: admin role, 3: super admin role).
            read_only (int, optional): Whether the role is read-only (0: no, 1: yes).
            rules (dict, optional): Role rules defining permissions.
        
        Returns:
            dict: API response containing the IDs of created roles.
        
        Example:
            >>> role = zapi.roles.create(
            ...     name="Operator Role",
            ...     type=1
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/role/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, roleid):
        """
        Delete roles.
        
        Args:
            roleid (str|list): ID or list of IDs of roles to delete.
        
        Returns:
            dict: API response containing the IDs of deleted roles.
        
        Example:
            >>> # Delete a single role
            >>> zapi.roles.delete(roleid="1")
            >>> 
            >>> # Delete multiple roles
            >>> zapi.roles.delete(roleid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/role/delete
        """
        return self._call(f"{self.API_METHOD}.delete", roleid=roleid)

    def get(self, roleid=None, **filters):
        """
        Retrieve roles according to the given parameters.
        
        Args:
            roleid (str|list, optional): Return only roles with the given IDs.
            
        Keyword Args (filters):
            selectRules (str|list, optional): Include role rules in the result.
            filter (dict, optional): Filter roles by given properties.
            search (dict, optional): Search roles by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing roles matching the criteria.
        
        Example:
            >>> # Get all roles
            >>> roles = zapi.roles.get()
            >>> 
            >>> # Get role with rules
            >>> role = zapi.roles.get(roleid="1", selectRules="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/role/get
        """
        return self._call(f"{self.API_METHOD}.get", roleid=roleid, **filters)
    
    def update(self, roleid, **params):
        """
        Update existing roles.
        
        Args:
            roleid (str): ID of the role to update.
            
        Keyword Args (params):
            name (str, optional): Name of the role.
            type (int, optional): Type of the role (1: user role, 2: admin role, 3: super admin role).
            read_only (int, optional): Whether the role is read-only (0: no, 1: yes).
            rules (dict, optional): Role rules defining permissions.
        
        Returns:
            dict: API response containing the IDs of updated roles.
        
        Example:
            >>> zapi.roles.update(
            ...     roleid="1",
            ...     name="Updated Role Name"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/role/update
        """
        return self._call(f"{self.API_METHOD}.update", roleid=roleid, **params)