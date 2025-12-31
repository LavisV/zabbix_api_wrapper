# resources/image.py
# https://www.zabbix.com/documentation/7.0/en/manual/api/reference/image

try:
    from ..base import ZabbixBase
except ImportError:
    from base import ZabbixBase

class ImageResource(ZabbixBase):
    def __init__(self, client):
        super().__init__(client)

    API_METHOD = "image"

    def create(self, **params):
        """
        Create new images.
        
        Keyword Args (params):
            name (str, required): Name of the image.
            imagetype (int, required): Image type (1: icon, 2: background image).
            image (str, required): Base64 encoded image data.
            image_file (str, optional): Image file path (alternative to image parameter).
        
        Returns:
            dict: API response containing the IDs of created images.
        
        Example:
            >>> image = zapi.images.create(
            ...     name="Server Icon",
            ...     imagetype=1,
            ...     image="base64_encoded_image_data"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/image/create
        """
        return self._call(f"{self.API_METHOD}.create", **params)
    
    def delete(self, imageid):
        """
        Delete images.
        
        Args:
            imageid (str|list): ID or list of IDs of images to delete.
        
        Returns:
            dict: API response containing the IDs of deleted images.
        
        Example:
            >>> # Delete a single image
            >>> zapi.images.delete(imageid="1")
            >>> 
            >>> # Delete multiple images
            >>> zapi.images.delete(imageid=["1", "2"])
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/image/delete
        """
        return self._call(f"{self.API_METHOD}.delete", imageid=imageid)

    def get(self, imageid=None, **filters):
        """
        Retrieve images according to the given parameters.
        
        Args:
            imageid (str|list, optional): Return only images with the given IDs.
            
        Keyword Args (filters):
            sysmapids (list, optional): Return only images used in the given maps.
            select_image (bool, optional): Include image data in the result.
            filter (dict, optional): Filter images by given properties.
            search (dict, optional): Search images by given properties (case-insensitive).
            output (str|list, optional): Object properties to be returned.
            countOutput (bool, optional): Return the number of records instead of actual data.
            sortfield (str|list, optional): Field to sort by.
            sortorder (str, optional): Sort order ("ASC" or "DESC").
            limit (int, optional): Limit the number of records returned.
        
        Returns:
            dict: API response containing images matching the criteria.
        
        Example:
            >>> # Get all images
            >>> images = zapi.images.get()
            >>> 
            >>> # Get image by ID with image data
            >>> image = zapi.images.get(imageid="1", select_image=True)
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/image/get
        """
        return self._call(f"{self.API_METHOD}.get", imageid=imageid, **filters)
        
    def update(self, imageid, **params):
        """
        Update existing images.
        
        Args:
            imageid (str): ID of the image to update.
            
        Keyword Args (params):
            name (str, optional): Name of the image.
            imagetype (int, optional): Image type (1: icon, 2: background image).
            image (str, optional): Base64 encoded image data.
            image_file (str, optional): Image file path (alternative to image parameter).
        
        Returns:
            dict: API response containing the IDs of updated images.
        
        Example:
            >>> zapi.images.update(
            ...     imageid="1",
            ...     name="Updated Image Name",
            ...     image="new_base64_encoded_image_data"
            ... )
        
        See Also:
            Zabbix API Documentation: https://www.zabbix.com/documentation/7.0/en/manual/api/reference/image/update
        """
        return self._call(f"{self.API_METHOD}.update", imageid=imageid, **params)