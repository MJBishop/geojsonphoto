import unittest
from geophoto.geojson_parser import GeoJSONParser


class TestGeoJSONParser(unittest.TestCase):

    def test_init_geojson_parser_collections_dictionary(self):
        geojson_parser = GeoJSONParser()
        self.assertEqual({}, geojson_parser._collections_dictionary)

    def test_add_first_feature(self):
        geojson_parser = GeoJSONParser()
        test_title = 'Test_Title'
        geojson_parser.add_feature(
            lat=0, long=0, properties={}, title = test_title
        )
        self.assertTrue(test_title in geojson_parser._collections_dictionary)


if __name__ == '__main__':
    unittest.main()