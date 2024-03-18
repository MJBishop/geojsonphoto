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

    
class TestParserArguments(unittest.TestCase):

    def setUp(self):
        self.parser = create_parser()

    def test_parser_short_in_path(self):
        parsed = self.parser.parse_args(['-i', 'testing/in'])
        self.assertEqual('testing/in', parsed.in_dir_path)

    def test_parser_in_path(self):
        parsed = self.parser.parse_args(['--in_dir_path', 'testing/in'])
        self.assertEqual('testing/in', parsed.in_dir_path)

    def test_parser_short_out_path(self):
        parsed = self.parser.parse_args(['-o', 'testing/out'])
        self.assertEqual('testing/out', parsed.out_dir_path)

    def test_parser_out_path(self):
        parsed = self.parser.parse_args(['--out_dir_path', 'testing/out'])
        self.assertEqual('testing/out', parsed.out_dir_path)

    def test_parser_short_save_images(self):
        parsed = self.parser.parse_args(['-s'])
        self.assertTrue(parsed.save_images)

    def test_parser_save_images(self):
        parsed = self.parser.parse_args(['--save_images'])
        self.assertTrue(parsed.save_images)

    def test_parser_no_save_images(self):
        parsed = self.parser.parse_args(['--no-save_images'])
        self.assertFalse(parsed.save_images)

    def test_parser_short_save_thumbnails(self):
        parsed = self.parser.parse_args(['-t'])
        self.assertTrue(parsed.save_thumbnails)

    def test_parser_save_thumbnails(self):
        parsed = self.parser.parse_args(['--save_thumbnails'])
        self.assertTrue(parsed.save_thumbnails)

    def test_parser_no_save_thumbnails(self):
        parsed = self.parser.parse_args(['--no-save_thumbnails'])
        self.assertFalse(parsed.save_thumbnails)

    def test_parser_defaults(self):
        parsed = self.parser.parse_args([])
        with self.assertRaises(AttributeError):
            parsed.in_dir_path
        with self.assertRaises(AttributeError):
            parsed.out_dir_path
        with self.assertRaises(AttributeError):
            parsed.save_images
        with self.assertRaises(AttributeError):
            parsed.save_thumbnails




    



if __name__ == '__main__':  
    unittest.main()             # pragma: no cover