# resources/settings.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/settings

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class SettingsResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "settings"

    def get(self, **params):
        """
        Get global Zabbix settings.
        
        Keyword Args (params):
            (No parameters required)
        
        Returns:
            dict: API response containing global settings.
        
        Example:
            >>> settings = zapi.settings.get()
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/settings/get
        """
        return self._call(f"{self.API_METHOD}.get", **params)
    
    def update(self, **params):
        """
        Update global Zabbix settings.
        
        Keyword Args (params):
            default_lang (str, optional): Default language.
            default_theme (str, optional): Default theme.
            search_limit (int, optional): Search/autocomplete results limit.
            max_in_table (int, optional): Max number of rows in table.
            server_check_interval (int, optional): Server check interval.
            work_period (str, optional): Work period.
            alert_usrgrpid (str, optional): User group for database down messages.
            event_expire (int, optional): Event expiration period in days.
            event_max_period (str, optional): Max period for event correlation.
            default_timezone (str, optional): Default timezone.
            refresh_unsupported (int, optional): Refresh unsupported items interval.
            snmptrap_logging (int, optional): Log SNMP traps (0: disabled, 1: enabled).
            server (str, optional): Zabbix server name.
            server_port (int, optional): Zabbix server port.
            log_level (int, optional): Log level (0-5).
            log_file (str, optional): Log file path.
            log_file_size (int, optional): Log file size in MB.
            (Additional settings parameters available - see Zabbix documentation)
        
        Returns:
            dict: API response confirming the update.
        
        Example:
            >>> zapi.settings.update(
            ...     default_lang="en_US",
            ...     default_theme="dark-theme"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/settings/update
        """
        return self._call(f"{self.API_METHOD}.update", **params)