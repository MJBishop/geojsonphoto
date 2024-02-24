'''

'''


'''

'''
NORTH_REF = 'N'
SOUTH_REF = 'S'
EAST_REF = 'E'
WEST_REF = 'W'
MAX_MINUTES = 59
MAX_SECONDS = 59
MIN_DMS = 0
MAX_LAT_DEGREES = 90
MAX_LONG_DEGREES = 180


def is_latitude(ref):
    '''

    '''
    return (ref == NORTH_REF or ref == SOUTH_REF)


def is_longitude(ref):
    '''

    '''
    return (ref == EAST_REF or ref == WEST_REF)


def dms_to_decimal(degrees, minutes, seconds, ref):
    '''
    Convert Degrees, Minutes, Seconds, Ref to Decimal


    '''
    if ref not in [NORTH_REF, SOUTH_REF, EAST_REF, WEST_REF]:
        raise ValueError(f'ValueError: Invalid GPS Reference {ref}, Expecting N, S, E or W')
    if minutes > MAX_MINUTES or minutes < MIN_DMS:
        raise ValueError(f'ValueError: Invalid Minutes {str(minutes)}, Should be positive and less than 60')
    if seconds > MAX_SECONDS or seconds < MIN_DMS:
        raise ValueError(f'ValueError: Invalid Seconds {str(seconds)}, Should be positive and less than 60')
    if degrees < MIN_DMS:
        raise ValueError(f'ValueError: Invalid Degrees {str(seconds)}, Should be positive')
    if is_latitude(ref) and degrees > MAX_LAT_DEGREES:
        raise ValueError(f'ValueError: Latitude {str(degrees) + ref}, cannot be greater than 90 degrees')
    elif is_longitude(ref) and degrees > MAX_LONG_DEGREES:
        raise ValueError(f'ValueError: Longitude {str(degrees) + ref}, cannot be greater than 180 degrees')
    
    return (degrees + minutes/60 + seconds/3600) * (-1 if ref == SOUTH_REF or ref == WEST_REF else 1)

