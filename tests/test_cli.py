"""
Tests for cli
"""

import unittest

from im2geojson.cli import create_parser


class TestCLI(unittest.TestCase):

    def test_create_parser(self):
        parser = create_parser()
        self.assertIsNotNone(parser)



if __name__ == '__main__':  
    unittest.main()             # pragma: no cover