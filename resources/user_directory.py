# resources/user_directory.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/userdirectory

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class UserDirectoryResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "userdirectory"

    def create(self, **params):
        """
        Create new user directories (authentication methods).
        
        Keyword Args (params):
            name (str, required): Name of the user directory.
            host (str, required): LDAP host or IdP entity ID for SAML.
            port (int, optional): LDAP port.
            base_dn (str, optional): LDAP base DN.
            search_attribute (str, optional): LDAP search attribute.
            bind_dn (str, optional): LDAP bind DN.
            bind_password (str, optional): LDAP bind password.
            description (str, optional): Description of the user directory.
            idp_type (int, optional): IdP type for SAML (0: Generic, 1: Microsoft Entra ID, 2: Okta, 3: OneLogin).
            search_filter (str, optional): LDAP search filter.
            start_tls (int, optional): Use STARTTLS for LDAP (0: no, 1: yes).
            sso_url (str, optional): SAML SSO service URL.
            slo_url (str, optional): SAML SLO service URL.
            username_attribute (str, optional): SAML username attribute.
            sp_entityid (str, optional): SAML SP entity ID.
            nameid_format (str, optional): SAML NameID format.
            sign_messages (int, optional): Sign SAML messages (0: no, 1: yes).
            sign_assertions (int, optional): Sign SAML assertions (0: no, 1: yes).
            sign_authn_requests (int, optional): Sign SAML authentication requests (0: no, 1: yes).
            sign_logout_requests (int, optional): Sign SAML logout requests (0: no, 1: yes).
            sign_logout_responses (int, optional): Sign SAML logout responses (0: no, 1: yes).
            encrypt_nameid (int, optional): Encrypt SAML NameID (0: no, 1: yes).
            encrypt_assertions (int, optional): Encrypt SAML assertions (0: no, 1: yes).
            user_username (str, optional): User attribute mapping for username.
            user_lastname (str, optional): User attribute mapping for last name.
            user_refresh_token (str, optional): User attribute mapping for refresh token.
            group_name (str, optional): Group attribute mapping for name.
            group_member (str, optional): Group attribute mapping for member.
            provision_status (int, optional): Enable user provisioning (0: disabled, 1: enabled).
            provision_media (list, optional): Media type mappings for provisioned users.
            provision_groups (list, optional): User group mappings for provisioned users.
            ldap_configured (int, optional): LDAP configured (0: no, 1: yes).
        
        Returns:
            dict: API response containing the IDs of created user directories.
        
        Example:
            >>> user_directory = zapi.user_directories.create(
            ...     name="LDAP Directory",
            ...     host="ldap.example.com",
            ...     port=389,
            ...     base_dn="dc=example,dc=com"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/userdirectory/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, userdirectoryid):
        """
        Delete user directories.
        
        Args:
            userdirectoryid (str|list): ID or list of IDs of user directories to delete.
        
        Returns:
            dict: API response containing the IDs of deleted user directories.
        
        Example:
            >>> # Delete a single user directory
            >>> zapi.user_directories.delete(userdirectoryid="1")
            >>> 
            >>> # Delete multiple user directories
            >>> zapi.user_directories.delete(userdirectoryid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/userdirectory/delete
        """
        return self._call(f"{self.API_METHOD}.delete", userdirectoryid=userdirectoryid)

    def get(self, userdirectoryid=None, **filters):
        """
        Retrieve user directories according to the given parameters.
        
        Args:
            userdirectoryid (str|list, optional): Return only user directories with the given IDs.
            
        Keyword Args (filters):
            filter (dict, optional): Filter user directories by given properties.
            search (dict, optional): Search user directories by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing user directories matching the criteria.
        
        Example:
            >>> # Get all user directories
            >>> user_directories = zapi.user_directories.get()
            >>> 
            >>> # Get user directory by ID
            >>> user_directory = zapi.user_directories.get(userdirectoryid="1")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/userdirectory/get
        """
        return self._call(f"{self.API_METHOD}.get", userdirectoryid=userdirectoryid, **filters)

    def test(self, **params):
        """
        Test user directory connection and authentication.
        
        Keyword Args (params):
            userdirectoryid (str, optional): ID of the user directory to test.
            test_access (int, optional): Test access (0: no, 1: yes).
            user_name (str, optional): Username to test authentication.
            user_password (str, optional): Password to test authentication.
        
        Returns:
            dict: API response containing test results.
        
        Example:
            >>> result = zapi.user_directories.test(
            ...     userdirectoryid="1",
            ...     user_name="testuser",
            ...     user_password="password"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/userdirectory/test
        """
        return self._call(f"{self.API_METHOD}.test", **params)
    
    def update(self, userdirectoryid, **params):
        """
        Update existing user directories.
        
        Args:
            userdirectoryid (str): ID of the user directory to update.
            
        Keyword Args (params):
            name (str, optional): Name of the user directory.
            host (str, optional): LDAP host or IdP entity ID for SAML.
            port (int, optional): LDAP port.
            base_dn (str, optional): LDAP base DN.
            search_attribute (str, optional): LDAP search attribute.
            bind_dn (str, optional): LDAP bind DN.
            bind_password (str, optional): LDAP bind password.
            description (str, optional): Description of the user directory.
            idp_type (int, optional): IdP type for SAML.
            search_filter (str, optional): LDAP search filter.
            start_tls (int, optional): Use STARTTLS for LDAP.
            sso_url (str, optional): SAML SSO service URL.
            slo_url (str, optional): SAML SLO service URL.
            username_attribute (str, optional): SAML username attribute.
            sp_entityid (str, optional): SAML SP entity ID.
            nameid_format (str, optional): SAML NameID format.
            sign_messages (int, optional): Sign SAML messages.
            sign_assertions (int, optional): Sign SAML assertions.
            sign_authn_requests (int, optional): Sign SAML authentication requests.
            sign_logout_requests (int, optional): Sign SAML logout requests.
            sign_logout_responses (int, optional): Sign SAML logout responses.
            encrypt_nameid (int, optional): Encrypt SAML NameID.
            encrypt_assertions (int, optional): Encrypt SAML assertions.
            user_username (str, optional): User attribute mapping for username.
            user_lastname (str, optional): User attribute mapping for last name.
            user_refresh_token (str, optional): User attribute mapping for refresh token.
            group_name (str, optional): Group attribute mapping for name.
            group_member (str, optional): Group attribute mapping for member.
            provision_status (int, optional): Enable user provisioning.
            provision_media (list, optional): Media type mappings for provisioned users.
            provision_groups (list, optional): User group mappings for provisioned users.
            ldap_configured (int, optional): LDAP configured.
        
        Returns:
            dict: API response containing the IDs of updated user directories.
        
        Example:
            >>> zapi.user_directories.update(
            ...     userdirectoryid="1",
            ...     name="Updated Directory Name",
            ...     port=636
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/userdirectory/update
        """
        return self._call(f"{self.API_METHOD}.update", userdirectoryid=userdirectoryid, **params)
