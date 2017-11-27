import numpy
import sys
import string
# functions of getting location strings are not included yet 


def getLocation_green(longtitude,latitude):{
	
}

def getLocation_yellow():{
	
}

old_file_name = str(sys.argv[1])
new_file_name = str(sys.argv[2])
new_file = open(new_file_name,'rw')
for line in sys.stdin:
	line = line.strip()
	if len(line)==0:
		new_file.write("\t")
	if line[0] ="V":
		new_file.write(line)
		continue 
	line = line.split(",")
	if len(line)== 21:     #green taxi data
		if (float(line[5])==0 or float(line[6])==0 or float(line[7])==0 or float(line[8])==0):
			continue
		line = line[0]+","+line[1]+","+line[2]+","+getLocation_green(line[5],line[6])+","+getLocation_green(line[7],line[8])+ \
		","+line[9]+","+line[10]+","+line[11]+","+line[12]+"," +line[14]+","+line[15]+","+line[18]+","+line[19]
		new_file.write(line)
	if len(line)==17:
		line = line[0]+","+line[1]+","line[2]+","+getLocation_yellow(line[7])+","+getLocation_yellow(line[8])+","+\
		line[3]+","+line[4]+","+line[10]+","+line[11]+","+line[13]+","+line[14]+","+line[16]+","+line[9]
		new_file.write(line)
new_file.close()	



