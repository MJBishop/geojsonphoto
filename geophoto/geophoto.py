'''

'''
import os
import glob
from exif import Image
import io
from datetime import datetime
import json

from geophoto.geojson_parser import GeoJSONParser
from geophoto.dms_conversion import dms_to_decimal


'''

'''
DEFAULT_OUT_PATH = './'
OUT_DIR = 'geophoto_output/'
GEOJSON_OUT_DIR = 'geojson/'
IMAGE_OUT_DIR = 'images/'
THUMBNAIL_OUT_DIR = 'thumbnails/'


class GeoPhoto(object):
    '''
    
    '''
    def __init__(self, in_path, out_path=DEFAULT_OUT_PATH):
        '''
        
        '''
        self.in_path = in_path
        self.out_path = out_path
        self.geojson_parser = GeoJSONParser()

        for sub_dir in [GEOJSON_OUT_DIR, IMAGE_OUT_DIR, THUMBNAIL_OUT_DIR]:
            full_path = os.path.join(out_path, OUT_DIR, sub_dir)

            try:
                os.makedirs(full_path)
                print(f"Folder {full_path} created!")
            except FileExistsError:
                # print(f"Folder {full_path} already exists")
                pass


    