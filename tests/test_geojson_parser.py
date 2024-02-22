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
        self.assertEqual(1, len(geojson_parser._collections_dictionary[test_title]))

    def test_add_second_feature(self):
        geojson_parser = GeoJSONParser()
        test_title = 'Test_Title'
        geojson_parser.add_feature(
            lat=0, long=0, properties={}, title = test_title
        )
        geojson_parser.add_feature(
            lat=0, long=0, properties={}, title = test_title
        )
        self.assertEqual(2, len(geojson_parser._collections_dictionary[test_title]))



if __name__ == '__main__':
    unittest.main()