#!/usr/bin/env python

import sys
import string
import numpy
import csv
num = 0


def check_midtown(long,lati):
	if (-0.4193*long-lati+9.7473>=0):
		if(-0.4193*long-lati+9.7105<=0):
			if(1.2455*long-lati+132.9323>0):
				if(2.4849*long-lati+224.5396<0):
					return True
	return False











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

	if (check_midtown(float(line[3]),float(line[4]))):
		temp = line[1].split(" ")[1]
		temp = int(temp.split(':')[0])
		print("3.%s,1" %(temp))







