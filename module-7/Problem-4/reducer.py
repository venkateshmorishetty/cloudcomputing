#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

dictt = {}


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    words = line.split(", ")

    words[0] = words[0].strip("[")
    words[0] = words[0].strip("\"")

    words[1] = words[1].strip("]")
    words[1] = words[1].strip("\"")
    
    if words[0] not in dictt.keys():
        dictt[words[0]] = words[1][0:-10]


keys = list(dictt.keys())
values = list(dictt.values())

updatedvalues = set(values)
for i in updatedvalues:
    print "\""+i+"\""



