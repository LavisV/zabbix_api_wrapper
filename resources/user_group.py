# resources/user_group.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/usergroup

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class UserGroupResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "usergroup"

    def create(self, **params):
        """
        Create new user groups.
        
        Keyword Args (params):
            name (str, required): Name of the user group.
            rights (list, optional): Permissions for host groups. Each object should have id, permission.
            users (list, optional): Users to add to the user group. Each object should have a userid.
            tag_filters (list, optional): Tag-based permissions.
            gui_access (int, optional): GUI access permission level.
            users_status (int, optional): Status of users in the group (0: enabled, 1: disabled).
            debug_mode (int, optional): Whether debug mode is enabled (0: disabled, 1: enabled).
            mfa_status (int, optional): MFA status (0: disabled, 1: enabled).
        
        Returns:
            dict: API response containing the IDs of created user groups.
        
        Example:
            >>> group = zapi.user_groups.create(
            ...     name="Operators",
            ...     gui_access=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/usergroup/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, usergroupid):
        """
        Delete user groups.
        
        Args:
            usergroupid (str|list): ID or list of IDs of user groups to delete.
        
        Returns:
            dict: API response containing the IDs of deleted user groups.
        
        Example:
            >>> # Delete a single user group
            >>> zapi.user_groups.delete(usergroupid="7")
            >>> 
            >>> # Delete multiple user groups
            >>> zapi.user_groups.delete(usergroupid=["7", "8"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/usergroup/delete
        """
        return self._call(f"{self.API_METHOD}.delete", usergroupid=usergroupid)

    def get(self, usergroupid=None, **filters):
        """
        Retrieve user groups according to the given parameters.
        
        Args:
            usergroupid (str|list, optional): Return only user groups with the given IDs.
            
        Keyword Args (filters):
            userids (list, optional): Return only user groups that contain the given users.
            status (int, optional): Return only user groups with the given status (0: enabled, 1: disabled).
            selectUsers (str|list, optional): Include users in the result.
            selectRights (str|list, optional): Include permissions in the result.
            selectTagFilters (str|list, optional): Include tag filters in the result.
            filter (dict, optional): Filter user groups by given properties.
            search (dict, optional): Search user groups by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing user groups matching the criteria.
        
        Example:
            >>> # Get all user groups
            >>> groups = zapi.user_groups.get()
            >>> 
            >>> # Get user groups with users
            >>> groups = zapi.user_groups.get(selectUsers="extend")
            >>> 
            >>> # Get user groups by status
            >>> groups = zapi.user_groups.get(status=0)
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/usergroup/get
        """
        return self._call(f"{self.API_METHOD}.get", usergroupid=usergroupid, **filters)
    
    def update(self, usergroupid, **params):
        """
        Update existing user groups.
        
        Args:
            usergroupid (str): ID of the user group to update.
            
        Keyword Args (params):
            name (str, optional): Name of the user group.
            rights (list, optional): Permissions for host groups.
            users (list, optional): Users to replace existing ones.
            tag_filters (list, optional): Tag-based permissions.
            gui_access (int, optional): GUI access permission level.
            users_status (int, optional): Status of users in the group (0: enabled, 1: disabled).
            debug_mode (int, optional): Whether debug mode is enabled (0: disabled, 1: enabled).
            mfa_status (int, optional): MFA status (0: disabled, 1: enabled).
        
        Returns:
            dict: API response containing the IDs of updated user groups.
        
        Example:
            >>> zapi.user_groups.update(
            ...     usergroupid="7",
            ...     name="Updated Group Name",
            ...     gui_access=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/usergroup/update
        """
        return self._call(f"{self.API_METHOD}.update", usergroupid=usergroupid, **params)