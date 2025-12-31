# resources/service.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/service

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ServiceResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "service"

    def create(self, **params):
        """
        Create new services.
        
        Keyword Args (params):
            name (str, required): Name of the service.
            algorithm (int, required): Status calculation algorithm (0: do not calculate, 1: problem if at least one child has a problem, 2: problem if all children have problems).
            sortorder (int, required): Position of the service used for sorting.
            weight (int, optional): Weight of the service used to calculate status (only used when algorithm is 0).
            propagation_rule (int, optional): Status propagation rule (0: as is, 1: increase by, 2: decrease by, 3: ignore, 4: fixed).
            propagation_value (int, optional): Status propagation value (required if propagation_rule is 1, 2, or 4).
            description (str, optional): Description of the service.
            tags (list, optional): Service tags.
            problem_tags (list, optional): Problem tags.
            status_rules (list, optional): Status rules.
            parents (list, optional): Parent services. Each object should have a serviceid.
            children (list, optional): Child services. Each object should have a serviceid.
            times (list, optional): Service time periods.
        
        Returns:
            dict: API response containing the IDs of created services.
        
        Example:
            >>> service = zapi.services.create(
            ...     name="Web Service",
            ...     algorithm=1,
            ...     sortorder=0
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/service/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, serviceid):
        """
        Delete services.
        
        Args:
            serviceid (str|list): ID or list of IDs of services to delete.
        
        Returns:
            dict: API response containing the IDs of deleted services.
        
        Example:
            >>> # Delete a single service
            >>> zapi.services.delete(serviceid="1")
            >>> 
            >>> # Delete multiple services
            >>> zapi.services.delete(serviceid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/service/delete
        """
        return self._call(f"{self.API_METHOD}.delete", serviceid=serviceid)

    def get(self, serviceid=None, **filters):
        """
        Retrieve services according to the given parameters.
        
        Args:
            serviceid (str|list, optional): Return only services with the given IDs.
            
        Keyword Args (filters):
            parentids (list, optional): Return only services that are children of the given services.
            childids (list, optional): Return only services that are parents of the given services.
            selectParents (str|list, optional): Include parent services in the result.
            selectChildren (str|list, optional): Include child services in the result.
            selectTags (str|list, optional): Include tags in the result.
            selectProblemTags (str|list, optional): Include problem tags in the result.
            selectStatusRules (str|list, optional): Include status rules in the result.
            selectTimes (str|list, optional): Include time periods in the result.
            filter (dict, optional): Filter services by given properties.
            search (dict, optional): Search services by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing services matching the criteria.
        
        Example:
            >>> # Get all services
            >>> services = zapi.services.get()
            >>> 
            >>> # Get services with parent/child relationships
            >>> services = zapi.services.get(selectParents="extend", selectChildren="extend")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/service/get
        """
        return self._call(f"{self.API_METHOD}.get", serviceid=serviceid, **filters)
    
    def update(self, serviceid, **params):
        """
        Update existing services.
        
        Args:
            serviceid (str): ID of the service to update.
            
        Keyword Args (params):
            name (str, optional): Name of the service.
            algorithm (int, optional): Status calculation algorithm.
            sortorder (int, optional): Position of the service used for sorting.
            weight (int, optional): Weight of the service used to calculate status.
            propagation_rule (int, optional): Status propagation rule.
            propagation_value (int, optional): Status propagation value.
            description (str, optional): Description of the service.
            tags (list, optional): Service tags.
            problem_tags (list, optional): Problem tags.
            status_rules (list, optional): Status rules.
            parents (list, optional): Parent services.
            children (list, optional): Child services.
            times (list, optional): Service time periods.
        
        Returns:
            dict: API response containing the IDs of updated services.
        
        Example:
            >>> zapi.services.update(
            ...     serviceid="1",
            ...     name="Updated Service Name",
            ...     algorithm=2
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/service/update
        """
        return self._call(f"{self.API_METHOD}.update", serviceid=serviceid, **params)