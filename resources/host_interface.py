# resources/host_interface.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostinterface

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class HostInterfaceResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "hostinterface"

    def create(self, **params):
        """
        Create new host interfaces.
        
        Keyword Args (params):
            hostid (str, required): ID of the host the interface belongs to.
            dns (str, optional): DNS name used by the interface.
            ip (str, optional): IP address used by the interface.
            main (int, required): Whether the interface is used as default on the host (0: no, 1: yes).
            port (str, required): Port number used by the interface.
            type (int, required): Interface type (1: agent, 2: SNMP, 3: IPMI, 4: JMX).
            useip (int, required): Whether the connection should be made via IP (0: DNS, 1: IP).
            bulk (int, optional): Whether to use bulk SNMP requests (0: no, 1: yes).
            interfaceid (str, optional): ID of the host interface.
            details (dict, optional): Interface details (SNMP, IPMI, JMX specific).
        
        Returns:
            dict: API response containing the IDs of created host interfaces.
        
        Example:
            >>> interface = zapi.host_interfaces.create(
            ...     hostid="10105",
            ...     ip="192.168.1.1",
            ...     dns="",
            ...     main=1,
            ...     port="10050",
            ...     type=1,
            ...     useip=1
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostinterface/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, interfaceid):
        """
        Delete host interfaces.
        
        Args:
            interfaceid (str|list): ID or list of IDs of host interfaces to delete.
        
        Returns:
            dict: API response containing the IDs of deleted host interfaces.
        
        Example:
            >>> # Delete a single interface
            >>> zapi.host_interfaces.delete(interfaceid="1")
            >>> 
            >>> # Delete multiple interfaces
            >>> zapi.host_interfaces.delete(interfaceid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostinterface/delete
        """
        return self._call(f"{self.API_METHOD}.delete", interfaceid=interfaceid)

    def get(self, interfaceid=None, **filters):
        """
        Retrieve host interfaces according to the given parameters.
        
        Args:
            interfaceid (str|list, optional): Return only host interfaces with the given IDs.
            
        Keyword Args (filters):
            hostids (list, optional): Return only host interfaces that belong to the given hosts.
            itemids (list, optional): Return only host interfaces that are used by the given items.
            selectItems (str|list, optional): Include items in the result.
            filter (dict, optional): Filter host interfaces by given properties.
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing host interfaces matching the criteria.
        
        Example:
            >>> # Get all interfaces
            >>> interfaces = zapi.host_interfaces.get()
            >>> 
            >>> # Get interfaces for a host
            >>> interfaces = zapi.host_interfaces.get(hostids=["10105"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostinterface/get
        """
        return self._call(f"{self.API_METHOD}.get", interfaceid=interfaceid, **filters)

    def massadd(self, **params):
        """
        Mass add host interfaces to hosts.
        
        Keyword Args (params):
            hosts (list, required): Hosts to add interfaces to. Each object should have a hostid.
            interfaces (list, required): Host interfaces to add. Each interface should contain hostid, dns, ip, main, port, type, useip.
        
        Returns:
            dict: API response containing the IDs of updated hosts.
        
        Example:
            >>> zapi.host_interfaces.massadd(
            ...     hosts=[{"hostid": "10105"}],
            ...     interfaces=[{
            ...         "hostid": "10105",
            ...         "ip": "192.168.1.1",
            ...         "main": 1,
            ...         "port": "10050",
            ...         "type": 1,
            ...         "useip": 1
            ...     }]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostinterface/massadd
        """
        return self._call(f"{self.API_METHOD}.massadd", **params)

    def massremove(self, **params):
        """
        Mass remove host interfaces from hosts.
        
        Keyword Args (params):
            interfaceids (list, required): IDs of host interfaces to remove.
        
        Returns:
            dict: API response containing the IDs of deleted host interfaces.
        
        Example:
            >>> zapi.host_interfaces.massremove(interfaceids=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostinterface/massremove
        """
        return self._call(f"{self.API_METHOD}.massremove", **params)

    def replacehostinterfaces(self, **params):
        """
        Replace all host interfaces for the given hosts.
        
        Keyword Args (params):
            hostid (str, required): ID of the host to replace interfaces for.
            interfaces (list, required): Host interfaces to replace existing ones. Each interface should contain dns, ip, main, port, type, useip.
        
        Returns:
            dict: API response containing the IDs of updated hosts.
        
        Example:
            >>> zapi.host_interfaces.replacehostinterfaces(
            ...     hostid="10105",
            ...     interfaces=[{
            ...         "ip": "192.168.1.1",
            ...         "main": 1,
            ...         "port": "10050",
            ...         "type": 1,
            ...         "useip": 1
            ...     }]
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostinterface/replacehostinterfaces
        """
        return self._call(f"{self.API_METHOD}.replacehostinterfaces", **params)
    
    def update(self, interfaceid, **params):
        """
        Update existing host interfaces.
        
        Args:
            interfaceid (str): ID of the host interface to update.
            
        Keyword Args (params):
            hostid (str, optional): ID of the host the interface belongs to.
            dns (str, optional): DNS name used by the interface.
            ip (str, optional): IP address used by the interface.
            main (int, optional): Whether the interface is used as default on the host (0: no, 1: yes).
            port (str, optional): Port number used by the interface.
            type (int, optional): Interface type (1: agent, 2: SNMP, 3: IPMI, 4: JMX).
            useip (int, optional): Whether the connection should be made via IP (0: DNS, 1: IP).
            bulk (int, optional): Whether to use bulk SNMP requests (0: no, 1: yes).
            details (dict, optional): Interface details (SNMP, IPMI, JMX specific).
        
        Returns:
            dict: API response containing the IDs of updated host interfaces.
        
        Example:
            >>> zapi.host_interfaces.update(
            ...     interfaceid="1",
            ...     ip="192.168.1.2",
            ...     port="161"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostinterface/update
        """
        return self._call(f"{self.API_METHOD}.update", interfaceid=interfaceid, **params)