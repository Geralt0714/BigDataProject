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
	if float(line[9])==0:
		continue
	## prepare data
	year_P,month_P,date_P = line[1].split(" ")[0].split("-")
	year_P = int(year_P)
	month_P = int(month_P)
	date_P=int(date_P)
	hour_P,minu_P,seco_P = line[1].split(" ")[1].split(':')
	hour_P = int(hour_P)
	minu_P = int(minu_P)
	seco_P = int(seco_P)

	year_D,month_D,date_D = line[2].split(" ")[0].split("-")
	year_D = int(year_D)
	month_D = int(month_D)
	date_D = int(date_D)
	hour_D,minu_D,seco_D = line[2].split(" ")[1].split(':')
	hour_D = int(hour_D)
	minu_D = int(minu_D)
	seco_D = int(seco_D)
	Trip_distance=float(line[8])


	key=0
	value = 0
	if (float(line[8])==0 or float(line[9])==0):
		print("0-1,1")
		continue
	print('0-2,1')

## fees related mining
	if float(line[13])<15:
		print('1-1.1')
	if (float(line[13])>=15 and float(line[13])<40):
		print('1-2.1')
	if (float(line[13])>=40 and float(line[13])<70):
		print('1-3.1')
	if (float(line[13])>=70 and float(line[13])<100):
		print('1-4.1')
	if float(line[13])>=100 :
		print('1-5.1')
	## credit card vs cash
	if (line[14] != 'CRD' or line[14] =="1"):
		print('2-1,1')
		print('2-1-%s,1' %(month_P))
	else:
		print('2-2,1')
		print('2-2-%s,1' %(month_P))
		if (float(line[11])==0):
			print('2-3,1')
		else:
			percent = float(11)/float(9)
			if percent <1:
				print('2-4-%s,1'%(month_P))
				print('2-4-%s,%s'%(month_P,percent))
				print ('2-5,1')
				print('2-5-1,%s' %(percent))
				print('2-6-1-%s,%s'%(hour,percent))
				print('2-6-2-%s,1'%(hour))
	## income for taxi driver
	print("2-7-1,%s"%(line[9]))	
	print("2-7-2,%s"%(line[11]))

## location and time mining
	print("3-1-1,1")
	if (check_Manh(float(line[3]),float(line[4]))):
		print("3-1-2,1")
	if (check_midtown(float(line[3]),float(line[4]))):
		print("3-2-%s,1" %(hour_P))
		print("3-1-3,1")


	if (check_midtown(float(line[3]),float(line[4]))):
		if (check_midtown(float(line[5]),float(line[6])) != True):
			print("3-3-%s,1" %(hour_P))

	if (check_midtown(float(line[3]),float(line[4]))!=True):
		if (check_midtown(float(line[5]),float(line[6]))):
			print("3-4-%s,1" %(hour_P))

	if (check_Manh(float(line[3]),float(line[4]))):
		if (check_Manh(float(line[5]),float(line[6])) != True):
			print("3-5-%s,1" %(hour_P))

	if (check_Manh(float(line[3]),float(line[4]))!=True):
		if (check_Manh(float(line[5]),float(line[6]))):
			print("3-6-%s,1" %(hour_P))

   	# Midtown to LGA transportation condition
   	if (check_midtown(float(line[3]),float(line[4]))):
		if (check_LGA(float(line[5]),float(line[6]))):
			if(date_P==date_D):
				time = hour_D-hour_P + (minu_D - minu_P)/60
				if (time != 0 and float(line[8])!= 0 ): 
					speed = float(line[8])/time
					print("4-%s-1,%s" %(hour_P,time))
					print("4-%s-2,%s" %(hour_P,speed))
					print("4-%s-3,1" %(hour_P))
			else:
				time = hour_D+24-hour_P + (minu_D-minu_P)/60
				if (time !=0 and float(line[8])!=0):
					speed = float(line[8])/time
					print("4-%s-1,%s" %(hour_P,time))
					print("4-%s-2,%s" %(hour_P,speed))
					print("4-%s-3,1" %(hour_P))


	## midtown to JFK		

	if (check_midtown(float(line[3]),float(line[4]))):
		if (check_JFK(float(line[5]),float(line[6]))):
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
    #distribution of distance
	if (Trip_distance>0 and Trip_distance<=1):
		print("6-1,1")
	if (Trip_distance>1 and Trip_distance<=2):
		print("6-2,1")
	if (Trip_distance>2 and Trip_distance<=4):
		print("6-3,1")
	if (Trip_distance>4 and Trip_distance<=6):
		print("6-4,1")
	if (Trip_distance>4 and Trip_distance<=6):
		print("6-5,1")
	if (Trip_distance>6 and Trip_distance<=8):
		print("6-6,1")
	if (Trip_distance>8 and Trip_distance<=10):
		print("6-7,1")
	if (Trip_distance>10 and Trip_distance<=14):
		print("6-8,1")
	if (Trip_distance>14):
		print("6-9,1")




    #number of go to/leave manhaton with picktime
	if (check_Manh(float(line[3]),float(line[4]))):
		if not check_Manh(float(line[5]),float(line[6])):
			print("7-1-%s,1" %(hour_P))
	if not check_Manh(float(line[3]),float(line[4])):
		if check_Manh(float(line[5]),float(line[6])):
			print("7-2-%s,1" %(hour_P))





