"""

"""
import os
import glob
import json

from geophoto.geojson_parser import GeoJSONParser
from geophoto.exif_reader import read_exif

DEFAULT_OUT_DIR_PATH = './'
OUT_DIR = 'geophoto_output/'
GEOJSON_DIR = 'geojson/'
IMAGE_DIR = 'images/'


class GeoPhoto(object):
    """
    
    """

    def __init__(self, in_dir_path, out_dir_path=DEFAULT_OUT_DIR_PATH, images=False, thumbnails=False):
        # need: action_thumbnail!!
        """
        
        """
        self._in_dir_path = in_dir_path
        self._out_dir_path = out_dir_path
        self._images = images
        self._thumbnails = thumbnails
        self._geojson_parser = GeoJSONParser()

        # Make Output Directories
        dir_paths = [self.geojson_dir_path]
        if images or thumbnails:
            dir_paths.append(self.image_dir_path)
        for path in dir_paths:
            try:
                os.makedirs(path)
                # print(f"Folder {path} created!")
            except FileExistsError:
                # print(f"Folder {path} already exists")
                pass

    @property
    def in_dir_path(self):
        """Return the path to the input directory."""
        return self._in_dir_path
    
    @property
    def out_dir_path(self):
        """Return the path to the output directory."""
        return self._out_dir_path
    
    @property
    def geojson_dir_path(self):
        """Return the path to the geojson directory."""
        return os.path.join(self.out_dir_path, OUT_DIR, GEOJSON_DIR)
    
    @property
    def image_dir_path(self):
        """Return the path to the image directory."""
        return os.path.join(self.out_dir_path, OUT_DIR, IMAGE_DIR)
        
    def start(self):
        """
        
        """
        files = glob.iglob(f'{self.in_dir_path}**/*.[Jj][Pp][Gg]')

        for filepath in files:
            folder, coord, props = self._process_file(filepath)
            self._geojson_parser.add_feature(folder, *coord, props)

        # Save geojson
        for title, feature_collection in self._geojson_parser:
            geojson_file_path = os.path.join(self.geojson_dir_path, f'{title}.geojson')
            with open(geojson_file_path, 'w') as f:
                json.dump(feature_collection, f)

    def _process_file(self, filepath):
        try:
            coord, props, image_dict = read_exif(filepath)
        except:
            pass
            # return!
        else:
            folder, filename = GeoPhoto.folder_and_filename_from_filepath(filepath)

            # thumbnail 
            if self._thumbnails: # and thumbnail is not None:
                rel_thumbnail_path = self._rel_thumbnail_path(filename)
                thumbnail_path = os.path.join(self.out_dir_path, rel_thumbnail_path)

                with open(thumbnail_path, 'wb') as im:
                    im.write(image_dict['thumbnail'])
                    props["thumbnail_path"] = rel_thumbnail_path

            # image 
            if self._images: # and image is not None:
                rel_image_path = self._rel_image_path(filename)
                image_path = os.path.join(self.out_dir_path, rel_image_path)            

                with open(image_path, 'wb') as im:
                    im.write(image_dict['image'])
                    props["image_path"] = rel_image_path

            return folder, coord, props

    def _rel_image_path(self, filename):
        # Return the relative path to the image filename.
        return os.path.join(OUT_DIR, IMAGE_DIR, filename)
    
    def _rel_thumbnail_path(self, filename):
        # Return the relative path to the thumbnail image filename.
        thumb_file_name = GeoPhoto.thumbnail_filename_from_image_filename(filename)
        return os.path.join(OUT_DIR, IMAGE_DIR, thumb_file_name)

    @staticmethod
    def folder_and_filename_from_filepath(filepath):
        """Split the filepath and return the folder and filename."""
        head, filename = os.path.split(filepath)
        head, folder = os.path.split(head)
        return folder, filename
    
    @staticmethod
    def thumbnail_filename_from_image_filename(filename):
        """Split the image filename and return the thumbnail filename."""
        f_name, f_type  = filename.split('.')
        return f_name + '_thumb.' + f_type