'''

'''
from exif import Image
from datetime import datetime
import warnings 

from geophoto.dms_conversion import dms_to_decimal


def read_exif(image_file):
    '''
    
    '''
    image = Image(image_file)
    if not image.has_exif:
        # print(f'KeyError: No metadata in file {image_file.name}')
        raise KeyError


    # coord
    try:
        lat = dms_to_decimal(*image.gps_latitude, image.gps_latitude_ref)
        long = dms_to_decimal(*image.gps_longitude, image.gps_longitude_ref)
    except AttributeError as e:
        # print(f'AttributeError: Missing metadata, {e} in file {image_file.name}')
        raise e
    except ValueError as e:
        # print(f'{e}, in file {image_file.name}')
        raise e
    
    coord = (lat, long)
    

    # props : datetime
    try:
        datetime_object = datetime.strptime(image.datetime_original, '%Y:%m:%d %H:%M:%S')
    except AttributeError as e:
        # print(f'AttributeError: Missing metadata, {e} in file {image_file.name}')
        raise e
    except ValueError as e:
        # print(f'ValueError: {e}, in file {image_file.name}')
        raise e

    props = { "datetime": str(datetime_object) }


    # files
    files = {
        'image' : image.get_file(), 
        'thumbnail': image.get_thumbnail()
    }


    # delete exif data
    # Warning that not all data has been deleted:
    with warnings.catch_warnings():
        warnings.filterwarnings('error')
        try:
            image.delete_all()
        except Warning as e:
            # print(e) - log?
            pass

    return coord, props, files