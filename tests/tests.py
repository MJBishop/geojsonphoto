import unittest
import sys
sys.path.append("..")

import geophoto


class TestConvertDegreesMinutesSecondsToDecimal(unittest.TestCase):

    def test_convert_zero_east(self):
        test_decimal = 0
        self.assertEqual(test_decimal, geophoto.dms_to_decimal(0, 0, 0, 'E'))

    def test_convert_five_degrees_east(self):
        test_decimal = 5
        self.assertEqual(test_decimal, geophoto.dms_to_decimal(5, 0, 0, 'E'))

    def test_convert_five_degrees_twelve_minutes_north(self):
        test_decimal = 5.2
        self.assertEqual(test_decimal, geophoto.dms_to_decimal(5, 12, 0, 'N'))

    def test_convert_five_degrees_twelve_minutes_eighteen_seconds_north(self):
        test_decimal = 5.205
        self.assertEqual(test_decimal, geophoto.dms_to_decimal(5, 12, 18, 'N'))

    def test_convert_five_degrees_twelve_minutes_eighteen_seconds_south(self):
        test_decimal = -5.205
        self.assertEqual(test_decimal, geophoto.dms_to_decimal(5, 12, 18, 'S'))

    def test_convert_five_degrees_twelve_minutes_eighteen_seconds_west(self):
        test_decimal = -5.205
        self.assertEqual(test_decimal, geophoto.dms_to_decimal(5, 12, 18, 'W'))




if __name__ == '__main__':
    unittest.main()