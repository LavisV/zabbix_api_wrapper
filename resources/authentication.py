# resources/authentication.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/authentication
try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class AuthenticationResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "authentication"

    def get(self, **params):
        """
        Get authentication settings.
        
        Keyword Args (params):
            (No parameters required)
        
        Returns:
            dict: API response containing authentication settings.
        
        Example:
            >>> auth_settings = zapi.authentication.get()
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/authentication/get
        """
        return self._call(f"{self.API_METHOD}.get", **params)

    def update(self, **params):
        """
        Update authentication settings.
        
        Keyword Args (params):
            authentication_type (int, optional): Authentication method (0: internal, 1: LDAP, 2: SAML).
            http_auth_enabled (int, optional): Enable HTTP authentication (0: disabled, 1: enabled).
            http_case_sensitive (int, optional): HTTP authentication case sensitivity (0: insensitive, 1: sensitive).
            http_login_form (int, optional): HTTP login form (0: disabled, 1: enabled).
            http_strip_domains (str, optional): Comma-separated list of domain names to strip from HTTP username.
            http_autologin (int, optional): Enable HTTP autologin (0: disabled, 1: enabled).
            ldap_configured (int, optional): LDAP configured (0: no, 1: yes).
            ldap_host (str, optional): LDAP host.
            ldap_port (int, optional): LDAP port.
            ldap_base_dn (str, optional): LDAP base DN.
            ldap_search_attribute (str, optional): LDAP search attribute.
            ldap_bind_dn (str, optional): LDAP bind DN.
            ldap_bind_password (str, optional): LDAP bind password.
            ldap_case_sensitive (int, optional): LDAP case sensitivity (0: insensitive, 1: sensitive).
            saml_auth_enabled (int, optional): Enable SAML authentication (0: disabled, 1: enabled).
            saml_idp_entityid (str, optional): SAML IdP entity ID.
            saml_sso_url (str, optional): SAML SSO service URL.
            saml_slo_url (str, optional): SAML SLO service URL.
            saml_username_attribute (str, optional): SAML username attribute.
            saml_sp_entityid (str, optional): SAML SP entity ID.
            saml_nameid_format (str, optional): SAML NameID format.
            saml_sign_messages (int, optional): Sign SAML messages (0: no, 1: yes).
            saml_sign_assertions (int, optional): Sign SAML assertions (0: no, 1: yes).
            saml_sign_authn_requests (int, optional): Sign SAML authentication requests (0: no, 1: yes).
            saml_sign_logout_requests (int, optional): Sign SAML logout requests (0: no, 1: yes).
            saml_sign_logout_responses (int, optional): Sign SAML logout responses (0: no, 1: yes).
            saml_encrypt_nameid (int, optional): Encrypt SAML NameID (0: no, 1: yes).
            saml_encrypt_assertions (int, optional): Encrypt SAML assertions (0: no, 1: yes).
            saml_case_sensitive (int, optional): SAML case sensitivity (0: insensitive, 1: sensitive).
        
        Returns:
            dict: API response confirming the update.
        
        Example:
            >>> zapi.authentication.update(
            ...     authentication_type=0,
            ...     http_auth_enabled=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/authentication/update
        """
        return self._call(f"{self.API_METHOD}.update", **params)