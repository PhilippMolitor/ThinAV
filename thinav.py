#!/usr/bin/env python3

#
# Name...............ThinAV live filesystem antivirus scanner
# Author.............Lucas Roswora
#                    Philipp Molitor <https://phils-lab.io>
#

from livescanner import livescanner

if __name__ == '__main__':
    print("Loading ThinAV...")

    av = livescanner.LiveScanner()
    av.watch()
