'''

'''
import os
import glob
import json
import warnings 

from geophoto.geojson_parser import GeoJSONParser
from geophoto.exif_reader import read_exif


'''

'''
DEFAULT_OUT_DIR_PATH = './'
OUT_DIR = 'geophoto_output/'
GEOJSON_DIR = 'geojson/'
IMAGE_DIR = 'images/'


class GeoPhoto(object):
    '''
    
    '''
    def __init__(self, in_dir_path, out_dir_path=DEFAULT_OUT_DIR_PATH, images=False, thumbnails=False):
        # need: action_thumbnail!!
        '''
        
        '''
        self._in_dir_path = in_dir_path
        self._out_dir_path = out_dir_path
        self._images = images
        self._thumbnails = thumbnails
        self._geojson_parser = GeoJSONParser()

        # Make Output Directories
        sub_directories = [GEOJSON_DIR]
        if images or thumbnails:
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
            image_file = open(filepath, 'rb')
            try:
                coord, props, image_dict = read_exif(image_file)
                image_file.close()
            except:
                pass
            else:
                folder, filename = GeoPhoto.folder_and_filename_from_filepath(filepath)

                # thumbnail 
                if self._thumbnails:
                    rel_thumbnail_path = self._rel_thumbnail_path(filename)
                    thumbnail_path = os.path.join(self.out_dir_path, rel_thumbnail_path)

                    with open(thumbnail_path, 'wb') as im:
                        im.write(image_dict['thumbnail'])
                        props["thumbnail_path"] = rel_thumbnail_path

                # image 
                if self._images:
                    rel_image_path = self._rel_image_path(filename)
                    image_path = os.path.join(self.out_dir_path, rel_image_path)            

                    with open(image_path, 'wb') as im:
                        im.write(image_dict['image'])
                        props["image_path"] = rel_image_path

                # geojson
                self._geojson_parser.add_feature(folder, *coord, props)

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