#!/usr/bin/env python
"""mapper.py"""

import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    # words = line.split(", ")
    # increase counters
    print line