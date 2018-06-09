from watchdog.events import FileSystemEventHandler
from .comparator import Comparator


class AVWatchHandler(FileSystemEventHandler):
    """Watchdog handler class for ThinAV"""

    def __init__(self, callback):
        self.comparator = Comparator()
        self.callback = callback

    def on_created(self, event):
        self._scan(event)

    def on_modified(self, event):
        self._scan(event)

    def _scan(self, event):
        if event.is_directory is False:
            match, definition = self.comparator.get_definition(event.src_path)

            if match is True:
                self.callback(event.src_path, definition)
