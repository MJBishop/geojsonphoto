'''

'''
import os
import glob
from exif import Image
from datetime import datetime
import json
import warnings 

from geophoto.geojson_parser import GeoJSONParser
from geophoto.dms_conversion import dms_to_decimal


'''

'''
DEFAULT_OUT_DIR_PATH = './'
OUT_DIR = 'geophoto_output/'
GEOJSON_DIR = 'geojson/'
IMAGE_DIR = 'images/'


class GeoPhoto(object):
    '''
    
    '''
    def __init__(self, in_dir_path, out_dir_path=DEFAULT_OUT_DIR_PATH, strip_exif=True, resize=False, thumbnails=False):
        # need: action_thumbnail!!
        '''
        
        '''
        self._in_dir_path = in_dir_path
        self._out_dir_path = out_dir_path
        self.strip_exif = strip_exif
        self.resize = resize
        self.thumbnails = thumbnails
        self._geojson_parser = GeoJSONParser()

        # Make Output Directories
        sub_directories = [GEOJSON_DIR]
        if strip_exif or resize or thumbnails:
            sub_directories.append(IMAGE_DIR)

        for sub_dir in sub_directories:
            full_path = os.path.join(out_dir_path, OUT_DIR, sub_dir)

            try:
                os.makedirs(full_path)
                # print(f"Folder {full_path} created!")
            except FileExistsError:
                # print(f"Folder {full_path} already exists")
                pass

    @property
    def in_dir_path(self):
        return self._in_dir_path
    
    @property
    def out_dir_path(self):
        return self._out_dir_path
    
    @property
    def geojson_dir_path(self):
        return os.path.join(self.out_dir_path, OUT_DIR, GEOJSON_DIR)
    
    @property
    def image_dir_path(self):
        return os.path.join(self.out_dir_path, OUT_DIR, IMAGE_DIR)
        # either test for failure or always strip exif?
    
    def _rel_image_path(self, filename):
        return os.path.join(OUT_DIR, IMAGE_DIR, filename)
    
    def _rel_thumbnail_path(self, filename):
        thumb_file_name = GeoPhoto.thumbnail_filename_from_image_filename(filename)
        return os.path.join(OUT_DIR, IMAGE_DIR, thumb_file_name)
        


    def process(self):
        '''
        
        '''
        files = glob.iglob(f'{self.in_dir_path}**/*.[Jj][Pp][Gg]', recursive=False)

        for filepath in files:
            with open(filepath, 'rb') as image_file:
                image = Image(image_file)
                if image.has_exif:

                    # exif data
                    lat = dms_to_decimal(*image.gps_latitude, image.gps_latitude_ref)
                    long = dms_to_decimal(*image.gps_longitude, image.gps_longitude_ref)
                    datetime_object = datetime.strptime(image.datetime_original, '%Y:%m:%d %H:%M:%S')
                    props = {
                        "datetime": str(datetime_object)
                    }


                    # 
                    folder, filename = GeoPhoto.folder_and_filename_from_filepath(filepath)

                    # thumbnail 
                    if self.thumbnails:
                        rel_thumbnail_path = self._rel_thumbnail_path(filename)
                        thumbnail_path = os.path.join(self.out_dir_path, rel_thumbnail_path)

                        with open(thumbnail_path, 'wb') as im:
                            im.write(image.get_thumbnail())
                            props["thumbnail_path"] = rel_thumbnail_path

                    # image 
                    if self.strip_exif or self.resize:
                        rel_image_path = self._rel_image_path(filename)
                        image_path = os.path.join(self.out_dir_path, rel_image_path)

                        if self.resize:
                            # TODO - resize image
                            pass

                        # delete exif data
                        with warnings.catch_warnings():
                            warnings.filterwarnings('error')
                            try:
                                image.delete_all()
                            except Warning as e:
                                # print(e) - log?
                                pass

                        with open(image_path, 'wb') as im:
                            im.write(image.get_file())
                            props["image_path"] = rel_image_path


                    # geojson
                    self._geojson_parser.add_feature(folder, lat, long, props)

        # Save geojson
        for title, feature_collection in self._geojson_parser:
            geojson_file_path = os.path.join(self.geojson_dir_path, f'{title}.geojson')
            with open(geojson_file_path, 'w') as f:
                json.dump(feature_collection, f)

    @staticmethod
    def folder_and_filename_from_filepath(filepath):
        '''
        
        '''
        head, filename = os.path.split(filepath)
        head, folder = os.path.split(head)
        return folder, filename
    
    @staticmethod
    def thumbnail_filename_from_image_filename(file_name):
        '''
        
        '''
        f_name, f_type  = file_name.split('.')
        return f_name + '_thumb.' + f_type