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

    def __init__(self, 
                 in_dir_path, 
                 out_dir_path=DEFAULT_OUT_DIR_PATH, 
                 save_images=False, 
                 save_thumbnails=False):
        """
        Initialise Geophoto
        """
        self._in_dir_path = in_dir_path
        self._out_dir_path = out_dir_path
        self._save_images = save_images
        self._save_thumbnails = save_thumbnails
        self._geojson_parser = GeoJSONParser()
        self._in_progress = None

        # Make Output Directories
        dir_paths = [self.geojson_dir_path]
        if save_images or save_thumbnails:
            dir_paths.append(self.image_dir_path)
        for path in dir_paths:
            try:
                os.makedirs(path)
            except FileExistsError:
                # print(f"Folder {path} already exists")
                pass
            else:
                # print(f"Folder {path} created!")
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
    
    @property
    def status(self):
        if self._in_progress is None:
            print('Ready')
        elif self._in_progress:
            print('In Progress')
        elif not self._in_progress:
            print('Finished')
        
    def start(self):
        """
        Read and process the images from `in_dir_path`.

        Notes
        -----
        Saves the harvested metadata as geojson to 'out_dir_path`
        Optionally saves images without metadata and thumbnails.
        """
        if self._in_progress is not None:
            raise RuntimeError('Error: Too many calls to function')
        
        self._in_progress = True
        self.status

        files = glob.iglob(f'{self.in_dir_path}**/*.[Jj][Pp][Gg]')

        for filepath in files:
            try:
                folder, coord, props = self._process_image_file(filepath)
            except:
                pass
            else:
                self._geojson_parser.add_feature(folder, *coord, props)

        # Save geojson
        for title, feature_collection in self._geojson_parser:
            geojson_file_path = os.path.join(self.geojson_dir_path, f'{title}.geojson')
            with open(geojson_file_path, 'w') as f:
                json.dump(feature_collection, f)
        
        self._in_progress = False
        self.status

    def _process_image_file(self, filepath):
        try:
            coord, props, image_b, thumb_b = read_exif(filepath, 
                                                       get_image=self._save_images, 
                                                       get_thumbnail=self._save_thumbnails)
        except KeyError as e:
            # record failure: No exif data
            raise e
        except AttributeError as e:
            # record failure: Missing exif data
            raise e
        except ValueError as e:
            # record failure: Invalid exif data
            raise e
        else:
            folder, filename = GeoPhoto.folder_and_filename_from_filepath(filepath)

            # image 
            if self._save_images and image_b is not None:
                rel_image_path = self._rel_image_path(filename)
                image_path = os.path.join(self.out_dir_path, rel_image_path)            

                with open(image_path, 'wb') as im:
                    im.write(image_b)
                    props["image_path"] = rel_image_path

            # thumbnail 
            if self._save_thumbnails and thumb_b is not None:
                rel_thumbnail_path = self._rel_thumbnail_path(filename)
                thumbnail_path = os.path.join(self.out_dir_path, rel_thumbnail_path)

                with open(thumbnail_path, 'wb') as im:
                    im.write(thumb_b)
                    props["thumbnail_path"] = rel_thumbnail_path

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