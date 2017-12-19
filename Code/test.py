#!/usr/bin/env python

import sys
import string
import numpy
for line in sys.stdin:
	line = line.strip()
	if len(line)==0:
		continue
	if (line[0]=="V"or line[0]=='v'):
		continue
	line = line.split(",")

	print ('%s,1'%(line[14]))