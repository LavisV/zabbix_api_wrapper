# resources/configuration.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/configuration

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ConfigurationResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "configuration"

    def export(self, **filters):
        """
        Export Zabbix configuration.
        
        Keyword Args (filters):
            format (str, optional): Export format (xml, json, yaml).
            options (dict, optional): Export options. Keys may include: groups, hosts, templates, images, maps, mediaTypes, etc.
        
        Returns:
            dict: API response containing exported configuration data.
        
        Example:
            >>> config = zapi.configuration.export(
            ...     format="xml",
            ...     options={"groups": True, "hosts": True}
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/configuration/export
        """
        return self._call(f"{self.API_METHOD}.export", **filters)

    def import_configuration(self, **params):
        """
        Import Zabbix configuration.
        
        Keyword Args (params):
            format (str, required): Import format (xml, json, yaml).
            source (str, required): Configuration data to import (XML/JSON/YAML string).
            rules (dict, optional): Import rules. Keys may include: groups, hosts, templates, images, maps, mediaTypes, etc.
        
        Returns:
            dict: API response confirming the import.
        
        Example:
            >>> zapi.configuration.import_configuration(
            ...     format="xml",
            ...     source=xml_string,
            ...     rules={"groups": {"createMissing": True, "updateExisting": True}}
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/configuration/import
        """
        return self._call(f"{self.API_METHOD}.import", **params)

    def import_compare(self, **params):
        """
        Compare configuration before import.
        
        Keyword Args (params):
            format (str, required): Import format (xml, json, yaml).
            source (str, required): Configuration data to compare.
            rules (dict, optional): Import rules.
        
        Returns:
            dict: API response containing comparison results.
        
        Example:
            >>> comparison = zapi.configuration.import_compare(
            ...     format="xml",
            ...     source=xml_string
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/configuration/importcompare
        """
        return self._call(f"{self.API_METHOD}.importcompare", **params)