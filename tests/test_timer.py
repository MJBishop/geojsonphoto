import unittest

from geophoto.timer import Timer

class TestTimer(unittest.TestCase):

    def test_timer_init(self):
        timer = Timer()
        self.assertEqual(0, timer.elapsed_time)