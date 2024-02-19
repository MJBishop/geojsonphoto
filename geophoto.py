


def dms_to_decimal(degrees, minutes, seconds, ref='N'):
    return (degrees + minutes/60 + seconds/3600) * (-1 if ref == 'S' else 1)