NORTH_REF = 'N'
SOUTH_REF = 'S'
EAST_REF = 'E'
WEST_REF = 'W'

'''
Convert Degrees, Minutes, Seconds, Ref to Decimal


'''
def dms_to_decimal(degrees, minutes, seconds, ref):
    if ref not in [NORTH_REF, SOUTH_REF, EAST_REF, WEST_REF]:
        raise ValueError('Invalid Reference! Expecting N, S, E or W: ' + ref)
    if (ref == NORTH_REF or ref == SOUTH_REF) and degrees > 90:
        raise ValueError('Latitude cannot be greater than 90 degrees: ' + str(degrees) + ref)
    elif (ref == EAST_REF or ref == WEST_REF) and degrees > 180:
        raise ValueError('Longitude cannot be greater than 180 degrees: ' + str(degrees) + ref)
    
    return (degrees + minutes/60 + seconds/3600) * (-1 if ref == SOUTH_REF or ref == WEST_REF else 1)


'''

'''
def lat_long_to_decimal(lat, lat_ref, long, long_ref):
    return 0, 0