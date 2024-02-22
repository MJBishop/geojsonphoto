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
MAX_LONG_DEGREES = 90


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
        raise ValueError('Invalid Reference! Expecting N, S, E or W: ' + ref)
    if minutes > MAX_MINUTES or minutes < MIN_DMS:
        raise ValueError('Invalid Minutes! Should be positive and less than 60: ' + str(minutes))
    if seconds > MAX_SECONDS or seconds < MIN_DMS:
        raise ValueError('Invalid Seconds! Should be positive and less than 60: ' + str(seconds))
    if degrees < MIN_DMS:
        raise ValueError('Invalid Degrees! Should be positive: ' + str(seconds))
    if is_latitude(ref) and degrees > MAX_LAT_DEGREES:
        raise ValueError('Latitude cannot be greater than 90 degrees: ' + str(degrees) + ref)
    elif is_longitude(ref) and degrees > MAX_LONG_DEGREES:
        raise ValueError('Longitude cannot be greater than 180 degrees: ' + str(degrees) + ref)
    
    return (degrees + minutes/60 + seconds/3600) * (-1 if ref == SOUTH_REF or ref == WEST_REF else 1)

