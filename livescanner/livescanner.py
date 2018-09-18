import time
from .avwatchhandler import AVWatchHandler
from watchdog.observers import Observer


class LiveScanner(object):
    """ThinAV live file scanner module"""

    def __init__(self, path):
        self.scan_path = path
        print("Spawned livescanner for directory {}".format(path))

    def watch(self):
        handler = AVWatchHandler(self.handle_found_file)

        observer = Observer()
        observer.schedule(handler, self.scan_path, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nTerminating ThinAV threads...")
            observer.stop()

        observer.join()

    def handle_found_file(self, path, definition):
        print('Found signature "{}" at "{}"!'.format(definition, path))
