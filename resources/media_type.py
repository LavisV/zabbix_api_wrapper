# resources/media_type.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/mediatype

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class MediaTypeResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "mediatype"

    def create(self, **params):
        """
        Create new media types.
        
        Keyword Args (params):
            name (str, required): Name of the media type.
            type (int, required): Media type (0: email, 1: script, 2: SMS, 3: Jabber, 100: Ez Texting, 4: Slack, 5: Teams, 6: Telegram, 7: webhook).
            smtp_server (str, optional): SMTP server host for email media type.
            smtp_port (int, optional): SMTP server port.
            smtp_helo (str, optional): SMTP HELO.
            smtp_email (str, optional): Email address from which notifications will be sent.
            smtp_security (int, optional): SMTP connection security (0: none, 1: STARTTLS, 2: SSL/TLS).
            smtp_verify_peer (int, optional): Verify peer for SMTP (0: no, 1: yes).
            smtp_verify_host (int, optional): Verify host for SMTP (0: no, 1: yes).
            smtp_authentication (int, optional): SMTP authentication (0: none, 1: normal password).
            username (str, optional): Username for authentication.
            passwd (str, optional): Password for authentication.
            gsm_modem (str, optional): Serial device name of the GSM modem.
            exec_path (str, optional): Script name or path.
            exec_params (str, optional): Script parameters.
            maxsessions (int, optional): Maximum number of sessions.
            maxattempts (int, optional): Maximum number of attempts.
            attempt_interval (str, optional): Attempt interval.
            content_type (int, optional): Content type (0: plain text, 1: HTML).
            script (str, optional): JavaScript for webhook media type.
            timeout (str, optional): Request timeout.
            process_tags (int, optional): Process tags (0: no, 1: yes).
            show_event_menu (int, optional): Show in event menu (0: no, 1: yes).
            event_menu_url (str, optional): Event menu URL.
            event_menu_name (str, optional): Event menu name.
            description (str, optional): Description of the media type.
            parameters (list, optional): Media type parameters for webhook.
            message_templates (list, optional): Message templates.
        
        Returns:
            dict: API response containing the IDs of created media types.
        
        Example:
            >>> media_type = zapi.media_types.create(
            ...     name="Email",
            ...     type=0,
            ...     smtp_server="smtp.example.com",
            ...     smtp_email="[email protected]"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/mediatype/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, mediatypeid):
        """
        Delete media types.
        
        Args:
            mediatypeid (str|list): ID or list of IDs of media types to delete.
        
        Returns:
            dict: API response containing the IDs of deleted media types.
        
        Example:
            >>> # Delete a single media type
            >>> zapi.media_types.delete(mediatypeid="1")
            >>> 
            >>> # Delete multiple media types
            >>> zapi.media_types.delete(mediatypeid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/mediatype/delete
        """
        return self._call(f"{self.API_METHOD}.delete", mediatypeid=mediatypeid)
    
    def get(self, mediatypeid=None, **filters):
        """
        Retrieve media types according to the given parameters.
        
        Args:
            mediatypeid (str|list, optional): Return only media types with the given IDs.
            
        Keyword Args (filters):
            filter (dict, optional): Filter media types by given properties.
            search (dict, optional): Search media types by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing media types matching the criteria.
        
        Example:
            >>> # Get all media types
            >>> media_types = zapi.media_types.get()
            >>> 
            >>> # Get media type by ID
            >>> media_type = zapi.media_types.get(mediatypeid="1")
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/mediatype/get
        """
        return self._call(f"{self.API_METHOD}.get", mediatypeid=mediatypeid, **filters)
    
    def update(self, mediatypeid, **params):
        """
        Update existing media types.
        
        Args:
            mediatypeid (str): ID of the media type to update.
            
        Keyword Args (params):
            name (str, optional): Name of the media type.
            type (int, optional): Media type.
            smtp_server (str, optional): SMTP server host for email media type.
            smtp_port (int, optional): SMTP server port.
            smtp_helo (str, optional): SMTP HELO.
            smtp_email (str, optional): Email address from which notifications will be sent.
            smtp_security (int, optional): SMTP connection security.
            smtp_verify_peer (int, optional): Verify peer for SMTP.
            smtp_verify_host (int, optional): Verify host for SMTP.
            smtp_authentication (int, optional): SMTP authentication.
            username (str, optional): Username for authentication.
            passwd (str, optional): Password for authentication.
            gsm_modem (str, optional): Serial device name of the GSM modem.
            exec_path (str, optional): Script name or path.
            exec_params (str, optional): Script parameters.
            maxsessions (int, optional): Maximum number of sessions.
            maxattempts (int, optional): Maximum number of attempts.
            attempt_interval (str, optional): Attempt interval.
            content_type (int, optional): Content type.
            script (str, optional): JavaScript for webhook media type.
            timeout (str, optional): Request timeout.
            process_tags (int, optional): Process tags (0: no, 1: yes).
            show_event_menu (int, optional): Show in event menu (0: no, 1: yes).
            event_menu_url (str, optional): Event menu URL.
            event_menu_name (str, optional): Event menu name.
            description (str, optional): Description of the media type.
            parameters (list, optional): Media type parameters for webhook.
            message_templates (list, optional): Message templates.
        
        Returns:
            dict: API response containing the IDs of updated media types.
        
        Example:
            >>> zapi.media_types.update(
            ...     mediatypeid="1",
            ...     name="Updated Email",
            ...     smtp_server="smtp.newserver.com"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/mediatype/update
        """
        return self._call(f"{self.API_METHOD}.update", mediatypeid=mediatypeid, **params)