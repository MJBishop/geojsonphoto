'''

'''
from exif import Image
from geophoto.dms_conversion import dms_to_decimal


def read_exif(image_file):
    '''
    
    '''
    image = Image(image_file)

    # coord
    lat = dms_to_decimal(*image.gps_latitude, image.gps_latitude_ref)
    long = dms_to_decimal(*image.gps_longitude, image.gps_longitude_ref)
    coord = (lat, long)

    # props
    props = {}


    # thumb
    thumb_f = None

    return coord, props, thumb_f