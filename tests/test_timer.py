import unittest
import io
from contextlib import redirect_stdout

from geophoto.timer import Timer


class TestTimer(unittest.TestCase):

    def test_timer_init(self):
        timer = Timer()
        self.assertEqual(0, timer.elapsed_time)

    def test_timer_status_ready(self):
        timer = Timer()
        f = io.StringIO()
        with redirect_stdout(f):
            timer.status()
        out = f.getvalue()

        self.assertEqual('Ready\n', out)

    def test_timer_status_running(self):
        timer = Timer()
        timer._in_progress = True
        f = io.StringIO()
        with redirect_stdout(f):
            timer.status()
        out = f.getvalue()

        self.assertEqual('Running...\n', out)

    def test_timer_status_finished(self):
        timer = Timer()
        timer._in_progress = False
        f = io.StringIO()
        with redirect_stdout(f):
            timer.status()
        out = f.getvalue()

        self.assertEqual('Finished in 0 seconds\n', out)