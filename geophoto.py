

'''
Convert Degrees, Minutes, Seconds, Ref to Decimal


'''
def dms_to_decimal(degrees, minutes, seconds, ref):
    if ref == 'N' and degrees > 90:
        raise ValueError('Latitude cannot be greater than 90 degrees: ' + str(degrees) + ref)
    
    return (degrees + minutes/60 + seconds/3600) * (-1 if ref == 'S' or ref == 'W' else 1)

    # if > 360 throw
    # if W and > 180:
        # return 360 - degrees
    # elif E and > 180:
        # return -360 + degrees

'''

'''
def lat_long_to_decimal(lat, lat_ref, long, long_ref):
    return 0, 0