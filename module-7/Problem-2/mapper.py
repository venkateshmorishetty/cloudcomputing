#!/usr/bin/env python
import sys
import json

def mapper(data):
	print data[0], data[1]

for line in sys.stdin:
	data = json.loads(line)
	mapper(data)
