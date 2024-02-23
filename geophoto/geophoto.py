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


    def process(self):
        '''
        
        '''
        files = glob.iglob(f'{self.in_path}**/*.[Jj][Pp][Gg]', recursive=False)

        for filepath in files:
            with open(filepath, 'rb') as image_file:
                image = Image(image_file)
                if image.has_exif:

                    folder, filename = GeoPhoto.folder_and_filename_from_filepath(filepath)


                    # geojson
                    lat = dms_to_decimal(*image.gps_latitude, image.gps_latitude_ref)
                    long = dms_to_decimal(*image.gps_longitude, image.gps_longitude_ref)
                    datetime_object = datetime.strptime(image.datetime_original, '%Y:%m:%d %H:%M:%S')
                    props = {
                        "datetime": str(datetime_object)
                    }
                    self.geojson_parser.add_feature(folder, lat, long, props)

        # Save geojson
        for title, feature_collection in self.geojson_parser:
            rel_g_path = os.path.join(OUT_DIR, GEOJSON_OUT_DIR, f'{title}.geojson')
            g_path = os.path.join(self.out_path, rel_g_path)
            with open(g_path, 'w') as f:
                json.dump(feature_collection, f)

    @classmethod
    def folder_and_filename_from_filepath(cls, filepath):
        '''
        
        '''
        head, filename = os.path.split(filepath)
        head, folder = os.path.split(head)
        return folder, filename
    
    @classmethod
    def thumbnail_filename_from_filename(cls, file_name):
        '''
        
        '''
        f_name, f_type  = file_name.split('.')
        return f_name + '_thumb.' + f_type