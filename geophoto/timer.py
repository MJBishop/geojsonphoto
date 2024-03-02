
from time import perf_counter


class Timer(object):

    def __init__(self):
        self.elapsed_time = 0
        self._in_progress = None

    def __enter__(self):
        self.start = perf_counter()
        self._in_progress = True
        self.status()
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop = perf_counter()
        self._in_progress = False
        self.elapsed_time = self.stop - self.start
        self.status()
        return False

    def status(self):
        if self._in_progress is None:
            print('Ready')
        elif self._in_progress:
            print('Running...')
        elif not self._in_progress:
            t = format(self.elapsed_time, '.2f')
            print(f'Finished in {t} seconds')

    @property
    def is_finished(self):
        return not self._in_progress