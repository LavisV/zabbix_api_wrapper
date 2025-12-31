# resources/user.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/user

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class UserResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "user"

    def checkauthentication(self, **params):
        """
        Check if authentication credentials are valid for a user.
        
        Keyword Args (params):
            sessionid (str, optional): User session ID to check.
            token (str, optional): API token to check.
        
        Returns:
            dict: API response indicating whether authentication is valid.
        
        Example:
            >>> result = zapi.users.checkauthentication(sessionid="abc123")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/user/checkauthentication
        """
        return self._call(f"{self.API_METHOD}.checkauthentication", **params)
    
    def create(self, **params):
        """
        Create new users.
        
        Keyword Args (params):
            username (str, required): Login name of the user.
            name (str, optional): Name of the user.
            surname (str, optional): Surname of the user.
            usrgrps (list, required): User groups to add the user to. Each object should have a usrgrpid.
            passwd (str, required): Password of the user.
            url (str, optional): URL of the page to redirect the user after logging in.
            autologin (int, optional): Whether to enable auto-login (0: disabled, 1: enabled).
            autologout (int, optional): User session life time in seconds (0: no logout).
            lang (str, optional): Language code for the user.
            refresh (str, optional): Automatic refresh period in seconds.
            theme (str, optional): UI theme (default, dark-theme, blue-theme).
            attempt_failed (int, optional): Number of consecutive failed login attempts.
            attempt_ip (str, optional): IP address from which the last failed login attempt was made.
            attempt_clock (int, optional): Time of the last failed login attempt.
            rows_per_page (int, optional): Number of rows per page.
            timezone (str, optional): User's timezone.
            roleid (str, required): ID of the user role.
            userdirectoryid (str, optional): Authentication method ID.
            medias (list, optional): Media to send notifications to.
                Each media object should contain: mediatypeid, sendto, active, severity, period
            mediatypes (list, optional): Media types to enable for the user.
            mfaid (str, optional): MFA method ID.
            mfa_status (int, optional): MFA status (0: disabled, 1: enabled).
        
        Returns:
            dict: API response containing the IDs of created users.
        
        Example:
            >>> user = zapi.users.create(
            ...     username="john.doe",
            ...     name="John",
            ...     surname="Doe",
            ...     passwd="secure_password",
            ...     usrgrps=[{"usrgrpid": "7"}],
            ...     roleid="1"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/user/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, userid):
        """
        Delete users.
        
        Args:
            userid (str|list): ID or list of IDs of users to delete.
        
        Returns:
            dict: API response containing the IDs of deleted users.
        
        Example:
            >>> # Delete a single user
            >>> zapi.users.delete(userid="1")
            >>> 
            >>> # Delete multiple users
            >>> zapi.users.delete(userid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/user/delete
        """
        return self._call(f"{self.API_METHOD}.delete", userid=userid)
    
    def get(self, userid=None, **filters):
        """
        Retrieve users according to the given parameters.
        
        Args:
            userid (str|list, optional): Return only users with the given IDs.
            
        Keyword Args (filters):
            selectMedias (str|list, optional): Include user medias in the result.
                - "extend": Include all user media properties
                - list: Return only the specified media properties
                - Example: selectMedias="extend" or selectMedias=["mediatypeid", "sendto"]
            
            selectUsrgrps (str|list, optional): Include user groups in the result.
                - "extend": Include all user group properties
                - list: Return only the specified user group properties
            
            selectMediatypes (str|list, optional): Include media types in the result.
            
            selectRole (str|list, optional): Include role information in the result.
            
            selectTimezone (bool, optional): Include timezone information.
            
            filter (dict, optional): Filter users by given properties.
                Example: filter={"alias": "admin", "status": "0"}
            
            search (dict, optional): Search users by given properties (case-insensitive).
                Example: search={"name": "John"}
            
            output (str|list, optional): Object properties to be returned.
                - "extend": Return all properties
                - list: Return only the specified properties
                - Example: output=["userid", "alias", "name"]
        
        Returns:
            dict: API response containing users matching the criteria.
        
        Example:
            >>> # Get all users with media information
            >>> users = zapi.users.get(selectMedias="extend")
            >>> 
            >>> # Get specific user by ID with groups
            >>> user = zapi.users.get(userid="1", selectUsrgrps="extend")
            >>> 
            >>> # Filter users by status
            >>> active_users = zapi.users.get(filter={"status": "0"})
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/user/get
        """
        return self._call(f"{self.API_METHOD}.get", userid=userid, **filters)

    def login(self, **params):
        """
        Authenticate and log in a user.
        
        Keyword Args (params):
            user (str, required): User name.
            password (str, required): User password.
            userData (bool, optional): Include user information in the response.
        
        Returns:
            dict: API response containing session ID and optionally user data.
        
        Example:
            >>> result = zapi.users.login(user="Admin", password="zabbix")
            >>> session_id = result["result"]
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/user/login
        """
        return self._call(f"{self.API_METHOD}.login", **params)
    
    def logout(self, **params):
        """
        Log out the current user.
        
        Keyword Args (params):
            (No parameters required, session is handled by client)
        
        Returns:
            dict: API response confirming logout.
        
        Example:
            >>> zapi.users.logout()
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/user/logout
        """
        return self._call(f"{self.API_METHOD}.logout", **params)

    def provision(self, **params):
        """
        Provision users from a user directory.
        
        Keyword Args (params):
            userdirectoryid (str, required): ID of the user directory.
            attributes (dict, optional): Attributes for user provisioning.
            userids (list, optional): IDs of specific users to provision.
        
        Returns:
            dict: API response containing provisioning results.
        
        Example:
            >>> zapi.users.provision(userdirectoryid="1")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/user/provision
        """
        return self._call(f"{self.API_METHOD}.provision", **params)
    
    def reset_totp(self, **params):
        """
        Reset TOTP (Time-based One-Time Password) for users.
        
        Keyword Args (params):
            userids (list, required): IDs of users to reset TOTP for.
        
        Returns:
            dict: API response containing the IDs of users with reset TOTP.
        
        Example:
            >>> zapi.users.reset_totp(userids=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/user/resettotp
        """
        return self._call(f"{self.API_METHOD}.resettotp", **params)

    def unblock(self, **params):
        """
        Unblock users who have been blocked after multiple failed login attempts.
        
        Keyword Args (params):
            userids (list, required): IDs of users to unblock.
        
        Returns:
            dict: API response containing the IDs of unblocked users.
        
        Example:
            >>> zapi.users.unblock(userids=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/user/unblock
        """
        return self._call(f"{self.API_METHOD}.unblock", **params)
    
    def update(self, userid, **params):
        """
        Update existing users.
        
        Args:
            userid (str): ID of the user to update.
            
        Keyword Args (params):
            username (str, optional): Login name of the user.
            name (str, optional): Name of the user.
            surname (str, optional): Surname of the user.
            usrgrps (list, optional): User groups to replace existing ones.
            passwd (str, optional): Password of the user.
            url (str, optional): URL of the page to redirect the user after logging in.
            autologin (int, optional): Whether to enable auto-login (0: disabled, 1: enabled).
            autologout (int, optional): User session life time in seconds (0: no logout).
            lang (str, optional): Language code for the user.
            refresh (str, optional): Automatic refresh period in seconds.
            theme (str, optional): UI theme (default, dark-theme, blue-theme).
            rows_per_page (int, optional): Number of rows per page.
            timezone (str, optional): User's timezone.
            roleid (str, optional): ID of the user role.
            userdirectoryid (str, optional): Authentication method ID.
            medias (list, optional): Media to replace existing ones.
            mediatypes (list, optional): Media types to enable for the user.
            mfaid (str, optional): MFA method ID.
            mfa_status (int, optional): MFA status (0: disabled, 1: enabled).
        
        Returns:
            dict: API response containing the IDs of updated users.
        
        Example:
            >>> zapi.users.update(
            ...     userid="1",
            ...     name="Updated Name",
            ...     theme="dark-theme"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/user/update
        """
        return self._call(f"{self.API_METHOD}.update", userid=userid, **params)