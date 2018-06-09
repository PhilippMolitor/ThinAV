#!/usr/bin/env python3

#
# Name...............ThinAV live filesystem antivirus scanner
# Author.............Lucas Roswora
#                    Philipp Molitor <https://phils-lab.io>
#

import config
from livescanner import livescanner

if __name__ == '__main__':
    print("Loading ThinAV...")

    av = livescanner.LiveScanner(config.tav_scan_path)
    av.watch()
