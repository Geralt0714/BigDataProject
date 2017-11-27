import numpy
import sys
import string
from geopy.geocoders import Nominatim
# functions of getting location strings are not included yet 

###################################
def getLocation_By_Coord(longtitude,latitude):
	
##################################
def getLocation_By_ID(Location_ID):

##################################
def cleanProcess(old_file_name,new_file_name,taxiType):
	new_file = open(new_file_name,'w')
	old_file = open(old_file_name,'r')
	for line in old_file:
		line = line.strip()
		if len(line)==0:
			new_file.write("\t")
			continue
		if line[0] ="V":
			new_file.write(line)
			continue 
		line = line.split(",")
		if taxiType =="green":		#green taxi data
			if len(line)== 21:     #2016_01-2016_06
				if (float(line[5])==0 or float(line[6])==0 or float(line[7])==0 or float(line[8])==0): #clean data
					continue
				line = line[0]+","+line[1]+","+line[2]+","+getLocation_By_Coord(float(line[5]),float(line[6]))+","+getLocation_By_Coord(line[7],line[8])+ \
				","+line[9]+","+line[10]+","+line[11]+","+line[12]+"," +line[14]+","+line[15]+","+line[18]+","+line[19]
				new_file.write(line)
				continue
			else:
				if len(line)==19:		#2016_07-2016_12
					line = line[0]+","+line[1]+","line[2]+","+getLocation_By_ID(int(line[5]))+","+getLocation_By_ID(int(line[6]))+","+\
					line[7]+","+line[8]+","+line[9]+","+line[10]+","+line[12]+","+line[13]+","+line[16]+","+line[17]
					new_file.write(line)
					continue
				else:
					print("format error in file:"+old_file_name)
					continue
		else:		#yellow taxi data
			if len(line)==19: 		#2016_01-2016_06
				if (float(line[5])==0 or float(line[6])==0 or float(line[9])==0 or float(line[10])==0): #clean data
					continue
				line = line[0]+","+line[1]+","+line[2]+","+getLocation_By_Coord(float(line[5]),float(line[6]))+","+getLocation_By_Coord(Float(line[9]),float(line[10]))+\
				","+line[3]+","+line[4]+","+line[12]+","+line[13]+","+line[15]+","+line[16]+","+line[18]+","+line[11]
				new_file.write(line)
				continue
			else:
				if len(line)==17:		#2016_07-2016_12
					line = line[0]+","+line[1]+","+line[2]+","+getLocation_By_ID(int(line[7]))+","+getLocation_By_ID(int(line[8]))+ \
					","+line[3]+","+line[4]+","+line[10]+","+line[11]+","+line[13]+","+line[14]+","+line[16]+","+line[9]
					new_file.write(line)
					continue
				else:
					print("format error in file:"+old_file_name)
					continue


	new_file.close()
	old_file.close()	

##############################
# main job function
for i in range(12):
	if i+1<10:
		old_file_name = "green_tripdata_2016-0"+ str(i+1)+".csv"
		new_file_name = "green_cleaned_2016-0"+str(i+1)+".csv"
		cleanProcess(old_file_name,new_file_name,"green")
		old_file_name = "yellow_tripdata_2016-0"+ str(i+1)+".csv"
		new_file_name = "yellow_cleaned_2016-0"+str(i+1)+".csv"
		cleanProcess(old_file_name,new_file_name,"yellow")
	else:
		old_file_name = "green_tripdata_2016-"+ str(i+1)+".csv"
		new_file_name = "green_cleaned_2016-"+str(i+1)+".csv"
		cleanProcess(old_file_name,new_file_name,"green")
		old_file_name = "yellow_tripdata_2016-"+ str(i+1)+".csv"
		new_file_name = "yellow_cleaned_2016-"+str(i+1)+".csv"
		cleanProcess(old_file_name,new_file_name,"yellow")





















