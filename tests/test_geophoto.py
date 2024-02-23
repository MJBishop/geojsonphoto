import unittest
import os
import shutil
from geophoto.geophoto import *


class TestGeoPhotoInit(unittest.TestCase):

    def setUp(self):
        self.in_path = 'tests/test_files/'
        self.out_path = 'tests/test_out_path/'

    def tearDown(self):
        out_path = os.path.join(self.out_path, OUT_DIR)
        if os.path.isdir(out_path):
            shutil.rmtree(out_path)

        default_path = os.path.join(DEFAULT_OUT_PATH, OUT_DIR)
        if os.path.isdir(default_path):
            shutil.rmtree(default_path)
    
    def test_init_geophoto_in_path(self):
        geophoto = GeoPhoto(in_path = self.in_path)
        self.assertEqual(self.in_path, geophoto.in_path)
    
    def test_init_geophoto_out_path(self):
        geophoto = GeoPhoto(in_path = self.in_path, out_path = self.out_path)
        self.assertEqual(self.out_path, geophoto.out_path)
    
    def test_init_geophoto_geojson_parser(self):
        geophoto = GeoPhoto(in_path = self.in_path, out_path = self.out_path)
        self.assertTrue(geophoto.geojson_parser)
    
    def test_default_init_geophoto_creates_out_directories(self):
        self.assertFalse(os.path.isdir(os.path.join(self.out_path, OUT_DIR)))

        geophoto = GeoPhoto(in_path = self.in_path, out_path = self.out_path)

        self.assertTrue(os.path.isdir(self.out_path))
        self.assertTrue(os.path.isdir(os.path.join(self.out_path, OUT_DIR)))
        self.assertTrue(os.path.isdir(os.path.join(self.out_path, OUT_DIR, GEOJSON_OUT_DIR)))

        self.assertFalse(os.path.isdir(os.path.join(self.out_path, OUT_DIR, IMAGE_OUT_DIR)))
        self.assertFalse(os.path.isdir(os.path.join(self.out_path, OUT_DIR, THUMBNAIL_OUT_DIR)))
        
# class TestGeoPhotoProcess(TestGeoPhotoInit):

#     def test_init_geophoto_process(self):
#         geophoto = GeoPhoto(in_path = self.in_path, out_path = self.out_path)
#         geophoto.process()


if __name__ == '__main__':
    unittest.main()