"""
Tests for cli
"""

import unittest

from im2geojson.cli import create_parser


class TestParserCreate(unittest.TestCase):

    def test_create_parser(self):
        parser = create_parser()
        self.assertIsNotNone(parser)

    def test_create_parser_prog(self):
        parser = create_parser()
        self.assertEqual('im2geojson', parser.prog)
        self.assertEqual('Geojson from image metadata', parser.description)
        # self.assertEqual('', parser.epilog)

    
class TestParserArguments(unittest.TestCase):

    def setUp(self):
        self.parser = create_parser()

    def test_parser_in_path(self):
        parsed = self.parser.parse_args(['testing'])
        self.assertEqual('testing', parsed.in_path)

    # def test_parse(self):
    #     parsed = self.parser.parse_args(['--something', 'test'])
    #     with self.assertRaises:
    #         self.assertEqual('test', parsed.something)

    



if __name__ == '__main__':  
    unittest.main()             # pragma: no cover