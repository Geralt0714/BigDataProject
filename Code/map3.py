#!/usr/bin/env python
##-73.700838   -74.255458 long range
## 40.496408  40.915587 lati range

import sys
import string
import numpy

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

## whole city coordinates range
long_w_max = -73.700838
long_w_min = -74.255458
lati_w_max = 40.915587
lati_w_min = 40.496408

long_w_range = long_w_max - long_w_min
lati_w_range = lati_w_max - lati_w_min


## manhatttan coords range
long_m_max = -73.908153
long_m_min = -74.022409
lati_m_max = 40.881219
lati_m_min = 40.700174

long_m_range = long_m_max - long_m_min
lati_m_range = lati_m_max - lati_m_min

## lower Manh coords range
long_lm_max = -73.955139
long_lm_min = -74.022409
lati_lm_max = 40.771585
lati_lm_min = 40.700174

long_lm_range = long_lm_max - long_lm_min
lati_lm_range = lati_lm_max - lati_lm_min

## JFK coord range
long_j_max = -73.767003
long_j_min = -73.813530
lati_j_max = 40.674099
lati_j_min = 40.636339

long_j_range = long_j_max - long_j_min
lati_j_range = lati_j_max - lati_j_min

## LGA coords range
long_l_max = -73.850634
long_l_min = -73.890697
lati_l_max = 40.784282
lati_l_min = 40.762611

long_l_range = long_l_max - long_l_min
lati_l_range = lati_l_max - lati_l_min


for line in sys.stdin:
        line = line.strip()
        if len(line)==0:
                continue
        if (line[0]=="V" or line[0]=="v"):
                continue
        line = line.split(',')
        longitude = float(line[3])
        latitude = float(line[4])
        xpixel = round((longitude-long_w_min)/long_w_range*3000)
        ypixel = round((latitude-lati_w_min)/lati_w_range*3000)

        print("%s %s 1\t1" %(xpixel,ypixel))

        if check_Manh(longitude,latitude):
        	xpixel = round((longitude-long_m_min)/long_m_range*3000)
        	ypixel = round((latitude-lati_m_min)/lati_m_range*3000)
        	print("%s %s 2\t1" %(xpixel,ypixel))

        	if (longitude>=long_lm_min and longitude <=long_lm_max):
        		if (latitude>=lati_lm_min and latitude< lati_lm_max):
        			xpixel = round((longitude-long_lm_min)/long_lm_range*3000)
        			ypixel = round((latitude-lati_lm_min)/lati_lm_range*3000)
        			print("%s %s 3\t1" %(xpixel,ypixel))

        if check_JFK(longitude,latitude):
        	xpixel = round((longitude-long_j_min)/long_j_range*3000)
        	ypixel = round((latitude-lati_j_min)/lati_j_range*3000)
        	print("%s %s 4\t1" %(xpixel,ypixel))

        if check_LGA(longitude,latitude):
        	xpixel = round((longitude-long_l_min)/long_l_range*3000)
        	ypixel = round((latitude-lati_l_min)/lati_l_range*3000)
        	print("%s %s 5\t1" %(xpixel,ypixel))


