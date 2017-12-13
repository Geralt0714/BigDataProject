#!/usr/bin/env python

import sys
import string
import numpy
import csv


def check_midtown(longitude,latitude):
	if (-0.4193*longitude-latitude+9.7473>=0):
		if(-0.4193*longitude-latitude+9.7105<=0):
			if(1.2455*longitude-latitude+132.9323>0):
				if(2.4849*longitude-latitude+224.5396<0):
					return True
	return False

def check_JFK(longitude,latitude):
	if(longitude<-73.767003 and longitude>-73.813530):
		if(latitude>40.636339 and latitude<40.674099):
			return True
	return False

def check_LGA(longitude,latitude):
	if(longitude>-73.890697 and longitude<-73.850634):
		if(latitude>40.762611 and latitude<40.784282):
			return True
	return False

def check_Manh(longitude,latitude):
	localcheck = 0
	if (latitude>0.2288*longitude+57.636):
		localcheck = localcheck+1
	if (latitude<2.9746*longitude+260.9168):
		localcheck = localcheck+1
	if (latitude<1.5787*longitude+157.6011):
		localcheck = localcheck+1
	if (latitude<-0.4242*longitude+9.5195):
		localcheck = localcheck+1
	## expect to be 4 for now
	## print(localcheck)
	if (longitude<=-73.974728):
		localcheck = localcheck+1
	if (longitude>-73.974728 and longitude<=-73.968720):
		if (latitude>5.5176*longitude+448.8712):
			localcheck = localcheck+1
	if (longitude>-73.968720 and longitude<=-73.933000):
		if (latitude>0.9003*longitude+107.3351):
			localcheck = localcheck+1
	if (longitude>-73.933000 and longitude<=-73.909755):
		if (latitude>1.6041*longitude+159.4296):
			localcheck = localcheck+1
		if (latitude>0.9003*longitude+107.3351):
			if (latitude<-0.6577*longitude-7.8183):
				localcheck = localcheck +1
	## expect to be 5 if in Manh
	## print(localcheck)

	if localcheck ==5 :
		return True
	else:
		return False


def check_downtown(longitude,latitude):
	if (-0.4193*longitude-latitude+9.7105>0):
		if check_Manh(longitude,latitude):
			return True
	else:
		return False

#######################################
## mapper function
for line in sys.stdin:
	line = line.strip()
	if len(line)==0:
		continue
	if (line[0]=="V"or line[0]=='v'):
		continue
	line = line.split(",")
	key=0
	value = 0
	if float(line[13])<15:
		key=1.1
		value = 1
	if (float(line[13])>=15 and float(line[13])<35):
		key = 1.2
		value = 1
	if (float(line[13])>=35 and float(line[13])<80):
		key = 1.3
		value = 1
	if float(line[13])>=80:
		key = 1.4
		value = 1

	print("%s,%s" %(key,value));

	if float(line[8])==0:
		print("6,1")

	

	if (float(line[11])==0):
		key = 2.1
		value = 1
	else:
		key = 2.2
		value = 1
	print("%s,%s" %(key,value));

	if (check_midtown(float(line[3]),float(line[4]))):
		temp = line[1].split(" ")[1]
		temp = int(temp.split(':')[0])
		print("3-%s,1" %(temp))
		print("4.1,1")
	else:
		print("4.2,1")

	if (check_midtown(float(line[3]),float(line[4]))):
		if (check_JFK(float(line[5]),float(line[6]))):
			time_P = line[1].split(" ")[1]
			date_P = line[1].split(" ")[0].split("-")[2]
			hour_P = int(time_P.split(':')[0])
			minu_P = int(time_P.split(':')[1])

			time_D = line[2].split(" ")[1]
			date_D = line[2].split(" ")[0].split("-")[2]
			hour_D = int(time_D.split(':')[0])
			minu_D = int(time_D.split(':')[1])

			print("5-%s,1" %(hour_P))
			if(date_P==date_D):
				time = hour_D-hour_P + (minu_D - minu_P)/60
				if (time != 0 and float(line[8])!= 0 ): 
					speed = float(line[8])/time
					print("5-%s-1,%s" %(hour_P,time))
					print("5-%s-2,%s" %(hour_P,speed))
					print("5-%s-3,1" %(hour_P))
			else:
				time = hour_D+24-hour_P + (minu_D-minu_P)/60
				if (time !=0 and float(line[8])!=0):
					speed = float(line[8])/time
					print("5-%s-1,%s" %(hour_P,time))
					print("5-%s-2,%s" %(hour_P,speed))
					print("5-%s-3,1" %(hour_P))





