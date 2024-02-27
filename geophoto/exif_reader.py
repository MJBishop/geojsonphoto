"""

"""
from exif import Image
from datetime import datetime
import warnings 

from geophoto.dms_conversion import dms_to_decimal


def read_exif(filepath):
    """
    Return exif metadata from image_file.


    
    Parameters
    ----------
    filepath : str
        The path to the image file.

    Returns
    -------
    coord : tuple of float
        The decimal representation of the latitude and longitude as a float.
    props : dictionary of str
        The quotient of the division.
    files : dictionary of bytes
        The quotient of the division.
    
    Raises
    ------
    KeyError
        If `ref` is invalid.
    AttributeError
        If `ref` is invalid.
        If `ref` is invalid.
    ValueError
        If `ref` is invalid.
        If `ref` is invalid.
    """

    with open(filepath, 'rb') as image_file:
        image = Image(image_file)
        if not image.has_exif:
            # print(f'KeyError: No metadata in file {image_file.name}')
            raise KeyError

        # coord
        try:
            dms_lat = (*image.gps_latitude, image.gps_latitude_ref)
            dms_long = (*image.gps_longitude, image.gps_longitude_ref)
        except AttributeError as e:
            # print(f'AttributeError: Missing coord metadata, {e} in file {image_file.name}')
            raise e
        else:
            try:
                lat = dms_to_decimal(*dms_lat)
                long = dms_to_decimal(*dms_long)
            except ValueError as e:
                # print(f'{e}, in file {image_file.name}')
                raise e
        
        # datetime
        try:
            datetime_str = image.datetime_original
        except AttributeError as e:
            # print(f'AttributeError: Missing metadata, {e} in file {image_file.name}')
            raise e
        else:
            try:
                datetime_object = datetime.strptime(datetime_str, '%Y:%m:%d %H:%M:%S')
            except ValueError as e:
                # print(f'ValueError: {e}, in file {image_file.name}')
                raise e

        # props 
        props = { 
            "datetime": str(datetime_object),
            }

        # files
        image_b = image.get_file()         # if image else None, 
        thumb_b = image.get_thumbnail() # if thumb else None, 

        # delete exif data
        with warnings.catch_warnings():
            # Warning that not all data has been deleted:
            warnings.filterwarnings('error')
            try:
                image.delete_all()
            except Warning as e:
                # print(e) - log?
                pass


        return (lat, long), props, image_b, thumb_b