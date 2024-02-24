'''

'''
from exif import Image
from geophoto.dms_conversion import dms_to_decimal
from datetime import datetime


def read_exif(image_file):
    '''
    
    '''
    image = Image(image_file)


    # coord
    try:
        lat = dms_to_decimal(*image.gps_latitude, image.gps_latitude_ref)
        long = dms_to_decimal(*image.gps_longitude, image.gps_longitude_ref)

    except KeyError as e:
        # print(f'KeyError: No metadata in file {image_file.name}')
        raise e
    
    except AttributeError as e:
        # print(f'AttributeError: Missing metadata, {e} in file {image_file.name}')
        raise e
    
    coord = (lat, long)
    

    # datetime
    try:
        datetime_object = datetime.strptime(image.datetime_original, '%Y:%m:%d %H:%M:%S')
    except AttributeError as e:
        # print(f'AttributeError: Missing metadata, {e} in file {image_file.name}')
        raise e

    # props
    props = {
        "datetime": str(datetime_object)
    }


    # thumb
    thumb_f = image.get_thumbnail()

    return coord, props, thumb_f