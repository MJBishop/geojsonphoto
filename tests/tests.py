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

    def test_lat_91N_raises_exception(self):
        with self.assertRaises(ValueError):
            geophoto.dms_to_decimal(91, 0, 0, 'N')

    def test_lat_91S_raises_exception(self):
        with self.assertRaises(ValueError):
            geophoto.dms_to_decimal(91, 0, 0, 'S')

    def test_long_181W_raises_exception(self):
        with self.assertRaises(ValueError):
            geophoto.dms_to_decimal(181, 0, 0, 'W')

    def test_long_181E_raises_exception(self):
        with self.assertRaises(ValueError):
            geophoto.dms_to_decimal(181, 0, 0, 'E')

    def test_invalid_ref_raises_exception(self):
        with self.assertRaises(ValueError):
            geophoto.dms_to_decimal(1, 1, 1, 'Z')

    def test_invalid_minutes_60_raises_exception(self):
        with self.assertRaises(ValueError):
            geophoto.dms_to_decimal(1, 60, 1, 'N')

    def test_invalid_negative_minutes_raises_exception(self):
        with self.assertRaises(ValueError):
            geophoto.dms_to_decimal(1, -1, 1, 'N')

    def test_invalid_seconds_60_raises_exception(self):
        with self.assertRaises(ValueError):
            geophoto.dms_to_decimal(1, 1, 60, 'N')



if __name__ == '__main__':
    unittest.main()