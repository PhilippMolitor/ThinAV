import time

from config import config
from .avwatchhandler import AVWatchHandler
from watchdog.observers import Observer


class LiveScanner(object):
    """
    ThinAV live file scanner module
    """

    def __init__(self):
        pass

    def watch(self):
        handler = AVWatchHandler(self.handle_found_file)

        observer = Observer()
        observer.schedule(handler, config.TAV_SCAN_PATH, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()

    def handle_found_file(self, path, definition):
        print('Found signature "{}" at "{}"!'.format(definition, path))
