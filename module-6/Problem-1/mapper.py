#!/usr/bin/env python

import sys
import json

def mapper(file):
	key = file[0]
	value = file[1].strip()
	charr = value.split()
	watch = {}
	for w in charr:
		middle = {}
		if (not watch.get(w,False)):
			watch[w]	= True
			middle.setdefault(w, [])
			middle[w].append(key)
			print w, middle[w]

for line in sys.stdin:
			file = json.loads(line)
			mapper(file)


