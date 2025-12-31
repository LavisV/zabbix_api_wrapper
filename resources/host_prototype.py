# resources/host_prototype.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HostPrototypeResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "hostprototype"

    def create(self, **params):
        """
        Create new host prototypes.
        
        Keyword Args (params):
            host (str, required): Technical name of the host prototype.
            ruleid (str, required): ID of the LLD rule that the host prototype belongs to.
            interfaces (list, required): Host interfaces for the host prototype.
            groupLinks (list, required): Host groups to add the host prototype to. Each object should have a groupid.
            groupPrototypes (list, optional): Host group prototypes. Each object should have a name.
            templates (list, optional): Templates to link to the host prototype. Each object should have a templateid.
            name (str, optional): Visible name of the host prototype.
            description (str, optional): Description of the host prototype.
            inventory (dict, optional): Host inventory properties.
            inventory_mode (int, optional): Host inventory population mode (-1: disabled, 0: manual, 1: automatic).
            tls_connect (int, optional): Connections to host.
            tls_accept (int, optional): Connections from host.
            tls_issuer (str, optional): Certificate issuer.
            tls_subject (str, optional): Certificate subject.
            tls_psk_identity (str, optional): PSK identity.
            tls_psk (str, optional): PSK value.
            macros (list, optional): User macros to assign to the host prototype.
            tags (list, optional): Tags to assign to the host prototype.
            status (int, optional): Status of the host prototype (0: enabled, 1: disabled).
            discovery_ruleid (str, required): ID of the LLD rule (alias for ruleid).
        
        Returns:
            dict: API response containing the IDs of created host prototypes.
        
        Example:
            >>> host_prototype = zapi.host_prototypes.create(
            ...     host="Server {#SERVER.NAME}",
            ...     ruleid="1",
            ...     interfaces=[{
            ...         "type": 1,
            ...         "main": 1,
            ...         "useip": 1,
            ...         "ip": "{#SERVER.IP}",
            ...         "dns": "",
            ...         "port": "10050"
            ...     }],
            ...     groupLinks=[{"groupid": "1"}]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, hostprototypeid):
        """
        Delete host prototypes.
        
        Args:
            hostprototypeid (str|list): ID or list of IDs of host prototypes to delete.
        
        Returns:
            dict: API response containing the IDs of deleted host prototypes.
        
        Example:
            >>> # Delete a single host prototype
            >>> zapi.host_prototypes.delete(hostprototypeid="1")
            >>> 
            >>> # Delete multiple host prototypes
            >>> zapi.host_prototypes.delete(hostprototypeid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/delete
        """
        return self._call(f"{self.API_METHOD}.delete", hostprototypeid=hostprototypeid)

    def get(self, hostprototypeid=None, **filters):
        """
        Retrieve host prototypes according to the given parameters.
        
        Args:
            hostprototypeid (str|list, optional): Return only host prototypes with the given IDs.
            
        Keyword Args (filters):
            discoveryids (list, optional): Return only host prototypes that belong to the given LLD rules.
            templateids (list, optional): Return only host prototypes that are linked to the given templates.
            selectGroupLinks (str|list, optional): Include host group links in the result.
            selectGroupPrototypes (str|list, optional): Include host group prototypes in the result.
            selectParentHost (str|bool, optional): Include parent host in the result.
            selectInterfaces (str|list, optional): Include host interfaces in the result.
            selectTemplates (str|list, optional): Include templates in the result.
            selectTags (str|list, optional): Include tags in the result.
            selectMacros (str|list, optional): Include macros in the result.
            selectDiscoveryRule (str|list, optional): Include LLD rule in the result.
            selectInventory (str|bool, optional): Include host inventory in the result.
            filter (dict, optional): Filter host prototypes by given properties.
            search (dict, optional): Search host prototypes by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing host prototypes matching the criteria.
        
        Example:
            >>> # Get all host prototypes
            >>> host_prototypes = zapi.host_prototypes.get()
            >>> 
            >>> # Get host prototypes for an LLD rule
            >>> host_prototypes = zapi.host_prototypes.get(discoveryids=["1"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/get
        """
        return self._call(f"{self.API_METHOD}.get", hostprototypeid=hostprototypeid, **filters)
    
    def update(self, hostprototypeid, **params):
        """
        Update existing host prototypes.
        
        Args:
            hostprototypeid (str): ID of the host prototype to update.
            
        Keyword Args (params):
            host (str, optional): Technical name of the host prototype.
            ruleid (str, optional): ID of the LLD rule that the host prototype belongs to.
            interfaces (list, optional): Host interfaces for the host prototype.
            groupLinks (list, optional): Host groups to replace existing ones.
            groupPrototypes (list, optional): Host group prototypes.
            templates (list, optional): Templates to replace existing ones.
            templates_clear (list, optional): Templates to unlink from the host prototype.
            name (str, optional): Visible name of the host prototype.
            description (str, optional): Description of the host prototype.
            inventory (dict, optional): Host inventory properties.
            inventory_mode (int, optional): Host inventory population mode.
            tls_connect (int, optional): Connections to host.
            tls_accept (int, optional): Connections from host.
            tls_issuer (str, optional): Certificate issuer.
            tls_subject (str, optional): Certificate subject.
            tls_psk_identity (str, optional): PSK identity.
            tls_psk (str, optional): PSK value.
            macros (list, optional): User macros to replace existing ones.
            tags (list, optional): Tags to replace existing ones.
            status (int, optional): Status of the host prototype (0: enabled, 1: disabled).
        
        Returns:
            dict: API response containing the IDs of updated host prototypes.
        
        Example:
            >>> zapi.host_prototypes.update(
            ...     hostprototypeid="1",
            ...     name="Updated Host Prototype Name",
            ...     status=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/update
        """
        return self._call(f"{self.API_METHOD}.update", hostprototypeid=hostprototypeid, **params)