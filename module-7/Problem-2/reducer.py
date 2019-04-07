#!/usr/bin/env python
import sys
 
output = {}
for line in sys.stdin:
	data = line.strip().split()
	if (data[0] in output): 
		output[data[0]].append(data[1])
	else:
		output[data[0]] = [data[1]]

for keys in output:
	print keys, len(output[keys])

