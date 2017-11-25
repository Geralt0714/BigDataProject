#!/usr/bin/env python

import sys
import string
import numpy
import csv
num = 0
for line in sys.stdin:
	line = line.strip()
	if len(line)==0:
		continue
	if line[0]=="V":
		continue
	line = line.split(",")
	key=0
	value = 0
	if float(line[18])<15:
		key=1.1
		value = 1
	if (float(line[18])>=15 and float(line[18])<35):
		key = 1.2
		value = 1
	if (float(line[18])>=35 and float(line[18])<80):
		key = 1.3
		value = 1
	if float(line[18])>=80:
		key = 1.4
		value = 1

	print("%s,%s" %(key,value));
	

	if (float(line[14])==0):
		key = 2.1
		value = 1
	else:
		key = 2.2
		value = 1
	print("%s,%s" %(key,value));
