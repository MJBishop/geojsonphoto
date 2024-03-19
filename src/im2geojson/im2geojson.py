"""
im2geojson.py
"""
import os
import glob
import json
import concurrent.futures

from .geojson_parser import GeoJSONParser
from .exif_reader import read_exif
from .timer import Timer

DEFAULT_IN_DIR_PATH = './'
DEFAULT_OUT_DIR_PATH = './'
OUT_DIR = 'im2geojson_output/'
GEOJSON_DIR = 'geojson/'
IMAGE_DIR = 'images/'


class ImageToGeoJSON(object):
    """
    ImageToGeoJSON

    Attributes
    ----------
    Notes
    -----
    Saves the harvested metadata as geojson to 'out_dir_path`
    Optionally saves images without metadata and thumbnails.
    """

    def __init__(self, 
                 in_dir_path=DEFAULT_IN_DIR_PATH, 
                 out_dir_path=DEFAULT_OUT_DIR_PATH, 
                 save_images=False, 
                 save_thumbnails=False):
        
        self._in_dir_path = in_dir_path
        self._out_dir_path = out_dir_path
        self._save_images = save_images
        self._save_thumbnails = save_thumbnails

        self._geojson_parser = GeoJSONParser()
        self._timer = None
        self._errors = {}
        self._total_count = 0
        self._success_count = 0

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
        """str: Return the path to the input directory."""
        return self._in_dir_path
    
    @property
    def out_dir_path(self):
        """str: Return the path to the output directory."""
        return self._out_dir_path
    
    @property
    def geojson_dir_path(self):
        """str: Return the path to the geojson directory."""
        return os.path.join(self.out_dir_path, OUT_DIR, GEOJSON_DIR)
    
    @property
    def image_dir_path(self):
        """str: Return the path to the image directory."""
        return os.path.join(self.out_dir_path, OUT_DIR, IMAGE_DIR)

    @property
    def errors(self):
        """dict: Return the error dictionary or 'No errors'."""
        if self._errors == {}:
            return 'No errors'
        else:
            return self._errors
        
    @property
    def summary(self):
        """str: Return the summary string."""
        return f'{self._success_count} out of {self._total_count} images completed successfully'

    def start(self):
        """
        Read and process the images from `in_dir_path`.

        """
        if self._timer is not None:
            raise RuntimeError('Error: Too many calls to function')
        
        with Timer() as self._timer:
            self._process_files()
        print(self.summary)
            
    def _process_files(self):
        # Process image files concurrently
        files = glob.iglob(f'{self.in_dir_path}**/*.[Jj][Pp][Gg]')
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_path = {executor.submit(self._process_image_file, filepath): filepath for filepath in files}
            for future in concurrent.futures.as_completed(future_to_path):
                filepath = future_to_path[future]
                self._total_count += 1
                try:
                    folder, coord, props = future.result()
                except Exception as e:
                    self._add_file_to_errors_with_exception_string(filepath, str(e))
                else:
                    self._geojson_parser.add_feature(folder, *coord, props)
                    self._success_count += 1

        # Save geojson
        for title, feature_collection in self._geojson_parser:
            geojson_file_path = os.path.join(self.geojson_dir_path, f'{title}.geojson')
            with open(geojson_file_path, 'w') as f:
                json.dump(feature_collection, f)

    def _process_image_file(self, filepath):
        try:
            coord, props, image_b, thumb_b = read_exif(filepath, 
                                                       get_image=self._save_images, 
                                                       get_thumbnail=self._save_thumbnails)
        except FileNotFoundError as e:
            raise FileNotFoundError('FileNotFoundError: No such file or directory') from e
        except Exception as e:
            raise e
        else:
            props['original_image_absolute_path'] = filepath
            folder, filename = ImageToGeoJSON.folder_and_filename_from_filepath(filepath)

            # image 
            if self._save_images and image_b is not None:
                rel_image_path = self._rel_image_path(filename)
                image_path = os.path.join(self.out_dir_path, rel_image_path)            

                with open(image_path, 'wb') as im:
                    im.write(image_b)
                    props["rel_image_path"] = rel_image_path

            # thumbnail 
            if self._save_thumbnails and thumb_b is not None:
                rel_thumbnail_path = self._rel_thumbnail_path(filename)
                thumbnail_path = os.path.join(self.out_dir_path, rel_thumbnail_path)

                with open(thumbnail_path, 'wb') as im:
                    im.write(thumb_b)
                    props["rel_thumbnail_path"] = rel_thumbnail_path

            return folder, coord, props
        
    def _add_file_to_errors_with_exception_string(self, filepath, exception_string):
        folder, filename = ImageToGeoJSON.folder_and_filename_from_filepath(filepath)
        key = os.path.join(folder, filename)
        self._errors[key] = exception_string

    def _rel_image_path(self, filename):
        # Return the relative path to the image filename.
        return os.path.join(OUT_DIR, IMAGE_DIR, filename)
    
    def _rel_thumbnail_path(self, filename):
        # Return the relative path to the thumbnail image filename.
        thumb_file_name = ImageToGeoJSON.thumbnail_filename_from_image_filename(filename)
        return os.path.join(OUT_DIR, IMAGE_DIR, thumb_file_name)

    @staticmethod
    def folder_and_filename_from_filepath(filepath):
        """tuple of str: Split the filepath and return the folder and filename."""
        head, filename = os.path.split(filepath)
        head, folder = os.path.split(head)
        return folder, filename
    
    @staticmethod
    def thumbnail_filename_from_image_filename(filename):
        """str: Split the image filename and return the thumbnail filename."""
        f_name, f_type  = filename.split('.')
        return f_name + '_thumb.' + f_type