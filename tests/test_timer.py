import unittest
from time import sleep
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

        self.assertEqual('Finished in 0.00 seconds\n', out)

    def test_timer_context_manager(self):
        f = io.StringIO()
        with redirect_stdout(f):
            with Timer() as timer:
                sleep(2)
        out = f.getvalue()

        self.assertEqual('Running...\nFinished in 2.00 seconds\n', out)

    def test_timer_is_finished(self):
        with Timer() as timer:
            pass
        self.assertTrue(timer.is_finished)