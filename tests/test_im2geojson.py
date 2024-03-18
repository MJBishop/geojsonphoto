"""
Tests for geojsonphoto
"""

import unittest
import os
import shutil
import io
from contextlib import redirect_stdout

from im2geojson.im2geojson import *


class TestImageToGeoJSONInit(unittest.TestCase):

    def setUp(self):
        self.default_in_path = "./"
        self.in_path = 'tests/test_files/test_images/test_exif/'
        self.out_path = 'tests/test_out_path/'
        self.geojson_dir_path = os.path.join(self.out_path, OUT_DIR, GEOJSON_DIR)
        self.image_dir_path = os.path.join(self.out_path, OUT_DIR, IMAGE_DIR)

    def tearDown(self):
        out_path = os.path.join(self.out_path, OUT_DIR)
        if os.path.isdir(out_path):
            shutil.rmtree(out_path)

        default_path = os.path.join(DEFAULT_OUT_DIR_PATH, OUT_DIR)
        if os.path.isdir(default_path):
            shutil.rmtree(default_path)
    
    def test_in_path(self):
        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path)
        self.assertEqual(self.in_path, im2geojson.in_dir_path)

    def test_default_in_path(self):
        im2geojson = ImageToGeoJSON()
        self.assertEqual(self.default_in_path, im2geojson.in_dir_path)
    
    def test_out_path(self):
        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, out_dir_path = self.out_path)
        self.assertEqual(self.out_path, im2geojson.out_dir_path)

    def test_init_creates_geojsonphoto_dir_path(self):
        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, out_dir_path = self.out_path)
        self.assertEqual(self.geojson_dir_path, im2geojson.geojson_dir_path)

    def test_init_creates_image_dir_path(self):
        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, out_dir_path = self.out_path)
        self.assertEqual(self.image_dir_path, im2geojson.image_dir_path)
    
    def test_init_geojsonphoto_parser(self):
        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, out_dir_path = self.out_path)
        self.assertTrue(im2geojson._geojson_parser)
    
    def test_default_init_im2geojson_creates_out_directories(self):
        self.assertFalse(os.path.isdir(os.path.join(self.out_path, OUT_DIR)))

        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, 
                            out_dir_path = self.out_path)

        self.assertTrue(os.path.isdir(self.geojson_dir_path))
        self.assertFalse(os.path.isdir(self.image_dir_path))
    
    def test_thumbnail_init_im2geojson_creates_out_directories(self):
        self.assertFalse(os.path.isdir(os.path.join(self.out_path, OUT_DIR)))

        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, 
                            out_dir_path = self.out_path, 
                            save_images=False, 
                            save_thumbnails=True)

        self.assertTrue(os.path.isdir(self.geojson_dir_path))
        self.assertTrue(os.path.isdir(self.image_dir_path))
    
    def test_image_init_im2geojson_creates_out_directories(self):
        self.assertFalse(os.path.isdir(os.path.join(self.out_path, OUT_DIR)))

        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, 
                            out_dir_path = self.out_path, 
                            save_images=True, 
                            save_thumbnails=False)

        self.assertTrue(os.path.isdir(self.geojson_dir_path))
        self.assertTrue(os.path.isdir(self.image_dir_path))
        

class TestImageToGeoJSONStart(TestImageToGeoJSONInit):

    def setUp(self):
        super().setUp()
        self.test_geojson_file_name = 'test_folder.geojson'

    def test_im2geojson_start_creates_geojsonphoto_file(self):
        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, 
                            out_dir_path = self.out_path, 
                            save_images=False)
        im2geojson.start()

        self.assertTrue(os.path.isdir(self.geojson_dir_path))

        geojson_path = os.path.join(self.geojson_dir_path, self.test_geojson_file_name)
        with open(geojson_path, 'r') as f:
            jsn = json.load(f)
            self.assertIsNotNone(jsn['features'][0]['properties']['datetime'])

            with self.assertRaises(KeyError):
                jsn['features'][0]['properties']['image_path']
            with self.assertRaises(KeyError):
                jsn['features'][0]['properties']['thumbnail_path']

    def test_im2geojson_start_creates_image_file(self):
        test_image_file = 'EXIF.jpg'
        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, 
                            out_dir_path = self.out_path, 
                            save_images=True)
        im2geojson.start()

        self.assertTrue(os.path.isdir(self.image_dir_path))

        image_path = os.path.join(self.image_dir_path, test_image_file)
        with open(image_path, 'r') as f:
            pass
        
        geojson_path = os.path.join(self.geojson_dir_path, self.test_geojson_file_name)
        with open(geojson_path, 'r') as f:
            jsn = json.load(f)
            self.assertIsNotNone(jsn['features'][0]['properties']['datetime'])
            self.assertIsNotNone(jsn['features'][0]['properties']['rel_image_path'])

            with self.assertRaises(KeyError):
                jsn['features'][0]['properties']['rel_thumbnail_path']

    def test_im2geojson_start_creates_thumbnail_file(self):
        test_thumbnail_file = 'EXIF_thumb.jpg'
        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, 
                            out_dir_path = self.out_path, 
                            save_images=False, 
                            save_thumbnails=True)
        im2geojson.start()

        self.assertTrue(os.path.isdir(self.image_dir_path))

        thumb_path = os.path.join(self.image_dir_path, test_thumbnail_file)
        with open(thumb_path, 'r') as f:
            pass
        
        geojson_path = os.path.join(self.geojson_dir_path, self.test_geojson_file_name)
        with open(geojson_path, 'r') as f:
            jsn = json.load(f)
            self.assertIsNotNone(jsn['features'][0]['properties']['datetime'])
            self.assertIsNotNone(jsn['features'][0]['properties']['rel_thumbnail_path'])

            with self.assertRaises(KeyError):
                jsn['features'][0]['properties']['rel_image_path']

    def test_geojsonphoto_start_original_image_absolute_path(self):
        test_thumbnail_file = 'EXIF_thumb.jpg'
        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, 
                            out_dir_path = self.out_path, 
                            save_images=False, 
                            save_thumbnails=False)
        im2geojson.start()

        geojson_path = os.path.join(self.geojson_dir_path, self.test_geojson_file_name)
        with open(geojson_path, 'r') as f:
            jsn = json.load(f)
            self.assertIsNotNone(jsn['features'][0]['properties']['original_image_absolute_path'])


class TestImageToGeoJSONStatus(TestImageToGeoJSONInit):

    def test_in_progress_status(self):
        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, 
                                 out_dir_path = self.out_path, 
                                 save_images=False, 
                                 save_thumbnails=True)
        f = io.StringIO()
        with redirect_stdout(f):
            im2geojson.start()
        out = f.getvalue()
        self.assertIn('Running...\nFinished in ', out)

    def test_repeat_calls_to_start_raises_exception(self):
        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, 
                                 out_dir_path = self.out_path, 
                                 save_images=False, 
                                 save_thumbnails=True)
        im2geojson.start()
        with self.assertRaises(RuntimeError):
            im2geojson.start()


class TestImageToGeoJSONErrors(TestImageToGeoJSONInit):
    
    def test_no_errors(self):
        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, 
                            out_dir_path = self.out_path, 
                            save_images=False, 
                            save_thumbnails=True)
        im2geojson.start()
        self.assertEqual('No errors', im2geojson.errors)
    
    def test_errors(self):
        in_path = 'tests/test_files/test_images/test_no_exif/'
        im2geojson = ImageToGeoJSON(in_dir_path = in_path, 
                            out_dir_path = self.out_path,
                            save_images=False, 
                            save_thumbnails=True)
        im2geojson.start()
        test_folder_file = 'test_folder/NO_EXIF.jpg'
        test_error_dictionary = {
            test_folder_file:"'No metadata.'"
        }
        self.assertEqual(test_error_dictionary, im2geojson.errors)


class TestImageToGeoJSONSummary(TestImageToGeoJSONInit):

    def test_summary(self):
        im2geojson = ImageToGeoJSON(in_dir_path = self.in_path, 
                            out_dir_path = self.out_path, 
                            save_images=False, 
                            save_thumbnails=True)
        im2geojson.start()
        self.assertEqual('1 out of 1 images completed successfully', im2geojson.summary)
        
        
class TestFolderFilesFromPath(unittest.TestCase):

    def setUp(self):
        self.test_filename = 'image_file.jpg'
        self.test_folder_filename = 'image_file_thumb.jpg'
        self.test_folder_name = 'folder'
        self.test_in_path = os.path.join('tests/test_files/', self.test_folder_name, self.test_filename)

    def test_filename_from_path(self):
        filename = ImageToGeoJSON.folder_and_filename_from_filepath(self.test_in_path)[1]
        self.assertEqual(self.test_filename, filename )

    def test_folder_from_path(self):
        folder = ImageToGeoJSON.folder_and_filename_from_filepath(self.test_in_path)[0]
        self.assertEqual(self.test_folder_name, folder)

    def test_thumbnail_filename_from_image_filename(self):
        thumbnail_filename = ImageToGeoJSON.thumbnail_filename_from_image_filename(self.test_filename)
        self.assertEqual(self.test_folder_filename, thumbnail_filename)



if __name__ == '__main__':
    unittest.main()             # pragma: no cover