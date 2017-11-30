import numpy
import sys
import string

###################################
## global variants 

long_max = -73.700838
long_min = -74.255458
lati_max = 40.915587
lati_min = 40.496408





##################################
def cleanProcess(old_file_name,new_file_name,taxiType):
	new_file = open(new_file_name,'w')
	old_file = open(old_file_name,'r')
	total_count = [0,0]
	error_count = [0,0,0,0,0]
	for line in old_file:
		line = line.strip()
		if len(line)==0:		#skip empty line
			continue
		if line[0] =="V":		#re-arrange columns order
			line = "VenderID,Pickup_time,Dropoff_time,Pickup_longitude,Pickup_latitude,Dropoff_longitude,Dropoff_latitude,"+\
			"PassengerCount,Trip_distance,Fare,Extra Fare,Tip,Tolls,TotalCharge,PaymentType\n"
			new_file.write(line)
			continue
		line = line.split(",")
		if taxiType =="green":		#green taxi data
			if (len(line)==20 or len(line)==21):     #make sure it's before 2016_07
				total_count[0] = total_count[0]+1
				if (float(line[5])==0 or float(line[6])==0 or float(line[7])==0 or float(line[8])==0): #clean data
					error_count[0] = error_count[0]+1
					continue
				if (float(line[5])<long_min or float(line[5])>long_max):
					error_count[1] = error_count[1]+1
					continue
				if (float(line[6])<lati_min or float(line[6])>lati_max):
					error_count[2] = error_count[2]+1
					continue
				if (float(line[7])<long_min or float(line[7])>long_max):
					error_count[3] = error_count[3]+1
					continue
				if (float(line[8])<lati_min or float(line[8])>lati_max):
					error_count[4] = error_count[4]+1
					continue

				line = line[0]+","+line[1]+","+line[2]+","+line[5]+","+line[6]+","+line[7]+","+line[8]+ \
				","+line[9]+","+line[10]+","+line[11]+","+line[12]+"," +line[14]+","+line[15]+","+line[len(line)-3]+","+line[len(line)-2]
				new_file.write(line)
				new_file.write("\n")
				total_count[1]=total_count[1]+1
				continue
			else:
				print("data frame length error")
		else:		#yellow taxi data
			if (len(line)==18 or len(line)==19): 		# make sure it's before 2016_07
				total_count[0] = total_count[0]+1
				if (float(line[5])==0 or float(line[6])==0 or float(line[7])==0 or float(line[8])==0): #clean data
					error_count[0] = error_count[0]+1
					continue
				if (float(line[5])<long_min or float(line[5])>long_max):
					error_count[1] = error_count[1]+1
					continue
				if (float(line[6])<lati_min or float(line[6])>lati_max):
					error_count[2] = error_count[2]+1
					continue
				if (float(line[7])<long_min or float(line[7])>long_max):
					error_count[3] = error_count[3]+1
					continue
				if (float(line[8])<lati_min or float(line[8])>lati_max):
					error_count[4] = error_count[4]+1
					continue
			line = line[0]+","+line[1]+","+line[2]+","+line[5]+","+line[6]+","+line[9]+","+line[10]+\
				","+line[3]+","+line[4]+","+line[12]+","+line[13]+","+line[15]+","+line[16]+","+line[len(line)-1]+","+line[11]
				new_file.write(line)
				new_file.write("\n")
				continue
			else:
				print("data frame length error")
	print("In file:"+old_file_name+" error_count are "+str(error_count)+"\t numbers are :"+str(total_count))
	new_file.close()
	old_file.close()	

##############################
def singleYearProcess(year):
	if int(year)<2016:				# we have 12 months data before year 2016
			for i in range(12):
				if i+1<10:
					old_file_name = "green_tripdata_"+year+"-0"+ str(i+1)+".csv"
					new_file_name = "green_cleaned_"+year+"-0"+str(i+1)+".csv"
					cleanProcess(old_file_name,new_file_name,"green")
					old_file_name = "yellow_tripdata_"+year+"-0"+ str(i+1)+".csv"
					new_file_name = "yellow_cleaned_"+year+"-0"+str(i+1)+".csv"
					cleanProcess(old_file_name,new_file_name,"yellow")
				else:
					old_file_name = "green_tripdata_"+year+"-"+ str(i+1)+".csv"
					new_file_name = "green_cleaned_"+year+"-"+str(i+1)+".csv"
					cleanProcess(old_file_name,new_file_name,"green")
					old_file_name = "yellow_tripdata_"+year+"-"+ str(i+1)+".csv"
					new_file_name = "yellow_cleaned_"+year+"-"+str(i+1)+".csv"
					cleanProcess(old_file_name,new_file_name,"yellow")

	if int(year)==2016:				# we only use Jan-Jun 2016 data beacause after Jun 2016 there are no location coordinates in data
		for i in range(7):
			old_file_name = "green_tripdata_"+year+"-0"+ str(i+1)+".csv"
			new_file_name = "green_cleaned_"+year+"-0"+str(i+1)+".csv"
			cleanProcess(old_file_name,new_file_name,"green")
			old_file_name = "yellow_tripdata_"+year+"-0"+ str(i+1)+".csv"
			new_file_name = "yellow_cleaned_"+year+"-0"+str(i+1)+".csv"
			cleanProcess(old_file_name,new_file_name,"yellow")


###############################
## main process function
for i in range(2014,2017):
	singleYearProcess(i)
















