


class Timer(object):

    def __init__(self):
        self.elapsed_time = 0
        self._in_progress = None


    def status(self):
        if self._in_progress is None:
            print('Ready')
        elif self._in_progress:
            print('Running...')
        elif not self._in_progress:
            print(f'Finished in {self.elapsed_time} seconds')