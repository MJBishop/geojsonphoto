'''

'''
from exif import Image
from geophoto.dms_conversion import dms_to_decimal
from datetime import datetime


def read_exif(image_file):
    '''
    
    '''
    image = Image(image_file)
    if not image.has_exif:
        raise KeyError(f'Error: No metadata in file {image_file.name}')

    # coord
    lat = dms_to_decimal(*image.gps_latitude, image.gps_latitude_ref)
    long = dms_to_decimal(*image.gps_longitude, image.gps_longitude_ref)
    coord = (lat, long)

    # props
    datetime_object = datetime.strptime(image.datetime_original, '%Y:%m:%d %H:%M:%S')
    props = {
        "datetime": str(datetime_object)
    }

    # thumb
    thumb_f = image.get_thumbnail()

    return coord, props, thumb_f