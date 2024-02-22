import unittest
from geophoto.geojson_parser import GeoJSONParser

class TestGeoJSONParser(unittest.TestCase):
    
    def test_init_geojson_parser(self):
        in_path = 'tests/test_files/IMG_9729.jpg'
        geojson_parser = GeoJSONParser(in_path = in_path)
        self.assertEqual(in_path, geojson_parser.in_path)


if __name__ == '__main__':
    unittest.main()