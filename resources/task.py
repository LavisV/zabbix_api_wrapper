# resources/task.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/task

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class TaskResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "task"

    def create(self, **params):
        """
        Create new tasks.
        
        Keyword Args (params):
            type (int, required): Task type (1: check now, 2: close problem, 3: acknowledge, 4: add host, 5: remove host, 6: add to maintenance, 7: remove from maintenance, 8: remote command, 9: data collection task, 10: remote command, 11: script execution, 12: configuration export, 13: configuration import, 14: delete host, 15: restart proxy).
            request (dict, required): Task request parameters. Contents depend on task type.
        
        Returns:
            dict: API response containing the IDs of created tasks.
        
        Example:
            >>> task = zapi.tasks.create(
            ...     type=1,
            ...     request={"itemid": "12345"}
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/task/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)

    def get(self, **params):
        """
        Retrieve tasks according to the given parameters.
        
        Keyword Args (params):
            taskids (list, optional): Return only tasks with the given IDs.
            type (int, optional): Return only tasks of the given type.
            status (int, optional): Return only tasks with the given status (0: new, 1: in progress, 2: completed, 3: failed).
            filter (dict, optional): Filter tasks by given properties.
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing tasks matching the criteria.
        
        Example:
            >>> # Get all tasks
            >>> tasks = zapi.tasks.get()
            >>> 
            >>> # Get tasks by status
            >>> tasks = zapi.tasks.get(status=1)
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/task/get
        """
        return self._call(f"{self.API_METHOD}.get", **params)