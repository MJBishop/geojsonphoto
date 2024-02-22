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
            collection_title = test_title, lat=0, long=0, properties={}
        )
        self.assertTrue(test_title in geojson_parser._collections_dictionary)
        self.assertEqual(1, len(geojson_parser._collections_dictionary[test_title]))

    def test_add_second_feature(self):
        geojson_parser = GeoJSONParser()
        test_title = 'Test_Title'
        geojson_parser.add_feature(
            collection_title = test_title, lat=0, long=0, properties={}
        )
        geojson_parser.add_feature(
            collection_title = test_title, lat=0, long=0, properties={}
        )
        self.assertEqual(2, len(geojson_parser._collections_dictionary[test_title]))

    def test_add_second_collection(self):
        geojson_parser = GeoJSONParser()
        test_title1 = 'Test_Title1'
        test_title2 = 'Test_Title2'
        geojson_parser.add_feature(
            collection_title = test_title1, lat=0, long=0, properties={}
        )
        geojson_parser.add_feature(
            collection_title = test_title2, lat=0, long=0, properties={}
        )
        self.assertEqual(1, len(geojson_parser._collections_dictionary[test_title1]))
        self.assertEqual(1, len(geojson_parser._collections_dictionary[test_title2]))



if __name__ == '__main__':
    unittest.main()