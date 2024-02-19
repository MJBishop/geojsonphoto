import unittest
import sys
sys.path.append("..")

import geophoto


class TestConvertDegreesMinutesSecondsToDecimal(unittest.TestCase):

    def test_convert_zero(self):
        test_decimal = 0
        self.assertEqual(test_decimal, geophoto.dms_to_decimal(0, 0, 0))

    def test_convert_five_degrees(self):
        test_decimal = 5
        self.assertEqual(test_decimal, geophoto.dms_to_decimal(5, 0, 0))

    def test_convert_five_degrees_twelve_minutes(self):
        test_decimal = 5.2
        self.assertEqual(test_decimal, geophoto.dms_to_decimal(5, 12, 0))

    def test_convert_five_degrees_twelve_minutes_eighteen_seconds(self):
        test_decimal = 5.205
        self.assertEqual(test_decimal, geophoto.dms_to_decimal(5, 12, 18))

    def test_convert_five_degrees_twelve_minutes_eighteen_seconds_south(self):
        test_decimal = -5.205
        self.assertEqual(test_decimal, geophoto.dms_to_decimal(5, 12, 18, 'S'))




if __name__ == '__main__':
    unittest.main()