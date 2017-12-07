#!/usr/bin/env python

import string
import sys
import numpy

currentkey = None
key = None
value = None
sum = 0
for line in sys.stdin:
	key, value = line.split(",")
	key = float(key)
	value = float(value)
	if currentkey==None:
		currentkey = key
	if key==currentkey :
		sum = sum + value
	else:
		print("%s,%s" %(currentkey,sum))
		sum = 0
		currentkey = key
if currentkey == key:
	print("%s,%s" %(currentkey,sum))
