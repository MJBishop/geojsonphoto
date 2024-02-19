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




if __name__ == '__main__':
    unittest.main()