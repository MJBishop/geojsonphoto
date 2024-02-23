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
    def __init__(self, in_path, out_path=DEFAULT_OUT_PATH, strip_exif=True, resize=False, thumbnails=False):
        '''
        
        '''
        self.in_path = in_path
        self.out_path = out_path
        self.strip_exif = strip_exif
        self.resize = resize
        self.thumbnails = thumbnails
        self.geojson_parser = GeoJSONParser()

        # Make Output Directories
        sub_directories = [GEOJSON_OUT_DIR]
        if strip_exif or resize:
            sub_directories.append(IMAGE_OUT_DIR)
        if thumbnails:
            sub_directories.append(THUMBNAIL_OUT_DIR)

        for sub_dir in sub_directories:
            full_path = os.path.join(out_path, OUT_DIR, sub_dir)

            try:
                os.makedirs(full_path)
                # print(f"Folder {full_path} created!")
            except FileExistsError:
                # print(f"Folder {full_path} already exists")
                pass



    @classmethod
    def folder_and_filename_from_filepath(cls, filepath):
        head, filename = os.path.split(filepath)
        head, folder = os.path.split(head)
        return folder, filename
    
    @classmethod
    def thumbnail_filename_from_filename(cls, file_name):
        file_name, file_type  = file_name.split('.')
        return file_name + '_thumb.' + file_type