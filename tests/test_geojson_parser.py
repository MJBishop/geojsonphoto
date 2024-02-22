import unittest
from geophoto.geojson_parser import GeoJSONParser


class TestGeoJSONParser(unittest.TestCase):

    def test_init_geojson_parser_collections_dictionary(self):
        geojson_parser = GeoJSONParser()
        self.assertEqual({}, geojson_parser._collections_dictionary)




if __name__ == '__main__':
    unittest.main()