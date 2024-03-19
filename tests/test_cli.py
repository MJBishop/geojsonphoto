"""
Tests for cli
"""

import unittest
import io
from contextlib import redirect_stdout

from im2geojson.cli import create_parser, parse_args_to_dict, main


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

    def test_parser_short_save_thumbnails(self):
        parsed = self.parser.parse_args(['-t'])
        self.assertTrue(parsed.save_thumbnails)

    def test_parser_save_thumbnails(self):
        parsed = self.parser.parse_args(['--save_thumbnails'])
        self.assertTrue(parsed.save_thumbnails)

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


class TestParseArgs(unittest.TestCase):

    def test_parsed_args_dict(self):
        args = ['-i', 'testing/in', '-o', 'testing/out', '-s', '-t']
        parsed_args_dict = parse_args_to_dict(args)
        expected = {'in_dir_path': 'testing/in', 
                    'out_dir_path': 'testing/out', 
                    'save_images': True, 
                    'save_thumbnails': True}
        self.assertEqual(expected, parsed_args_dict)


class TestMain(unittest.TestCase):

    def setUp(self):
        self.out_path = 'tests/test_out_path/'
    
    def test_main(self):
        f = io.StringIO()
        with redirect_stdout(f):
            
            main(['-o', self.out_path])
        out = f.getvalue()
        out_lines = out.split('\n')

        expected_first_line = 'Running...'
        expected_last_line = '0 out of 0 images completed successfully'

        self.assertEqual(expected_first_line, out_lines[0])
        self.assertEqual(expected_last_line, out_lines[2])


if __name__ == '__main__':  
    unittest.main()             # pragma: no cover