# resources/autoregistration.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/autoregistration

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class AutoRegistrationResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "autoregistration"

    def get(self, **filters):
        """
        Get autoregistration settings.
        
        Keyword Args (filters):
            (No parameters required)
        
        Returns:
            dict: API response containing autoregistration settings.
        
        Example:
            >>> autoreg_settings = zapi.autoregistration.get()
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/autoregistration/get
        """
        return self._call(f"{self.API_METHOD}.get", **filters)

    def update(self, **params):
        """
        Update autoregistration settings.
        
        Keyword Args (params):
            tls_accept (int, optional): Connections from agent (1: unencrypted, 4: PSK, 8: certificate).
            tls_psk_identity (str, optional): PSK identity.
            tls_psk (str, optional): PSK value.
            tls_issuer (str, optional): Certificate issuer.
            tls_subject (str, optional): Certificate subject.
        
        Returns:
            dict: API response confirming the update.
        
        Example:
            >>> zapi.autoregistration.update(
            ...     tls_accept=1,
            ...     tls_psk_identity="",
            ...     tls_psk=""
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/autoregistration/update
        """
        return self._call(f"{self.API_METHOD}.update", **params)