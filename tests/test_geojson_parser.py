import unittest
from geophoto.geojson_parser import GeoJSONParser

class TestGeoJSONParser(unittest.TestCase):
    
    def test_init_geojson_parser_in_path(self):
        in_path = 'tests/test_files/IMG_9729.jpg'
        geojson_parser = GeoJSONParser(in_path = in_path)
        self.assertEqual(in_path, geojson_parser.in_path)
    
    def test_init_geojson_parser_out_path(self):
        in_path = 'tests/test_files/IMG_9729.jpg'
        out_path = 'tests/test_out_path'
        geojson_parser = GeoJSONParser(in_path = in_path, out_path=out_path)
        self.assertEqual(out_path, geojson_parser.out_path)


if __name__ == '__main__':
    unittest.main()