# NYC Taxi Transportation Data Analysis
Big Data Analysis (CS-GY-9223) Course Project  

## Members
|Dingming Zhou	|Xinyu Wu		|Mufan Sang	|
|:-------------:|:-------------:|:---------:|
|dz1108			|xw1386		  	|ms9903 	|

## Data Collection
Data Source:[NYC Taxi & Limousine Commission Trip Record Data](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml)

## Part I: Data Cleaning
IMPORTANT!!!!!!:<br />
If your are using dumbo cluster at NYU HPC, please put the whole directory under /scratch/your-netid/ directory since the data files exceed the storage limit under /home/your-netid/ <br />
you can use `cd /scratch/your-netid/` to do that

#### To download raw Data  
`./download_raw_data.sh`  

#### Run data cleaning process  
`./data_clean.sh`  

In this process, it will create directory ./Data and ./Datacleaned to store the raw data and cleaned data files respectively<br />
These data files are stored locally, not in HDFS<br />

For more data cleaning details, see DataInfo.md

## Part II: Data Analysis

#### Push data file into HDFS
`hfs -put Datacleaned/.`
This could take a moment <br />
After pushing into hdfs, you can use `hfs -ls Datacleaned` to see the loaded data files<br />
We use sequence of hadoop job to do mapreduce since one-stage results has duplicate keys and too much time comsumption if use one reducer<br />

#### To process data of 2014, use <br />
`hjs \
	-files /scratch/YOUR-NETID/BigDataProject/Code \
	-mapper Code/map.sh \
	-reducer Code/reduce.sh \
	-input Datacleaned/yellow_2014.csv 
	-output temp2014.out
`
<br />
Then use<br />
`hfs -getmerge temp2014.out 2014.out` <br />
`hfs -put 2014.out`<br />

Then use<br />
`hjs \
	-D mapreduce.job.reduces=1 \
	-files /scratch/YOUR-NETID/BigDataProject/Code \
	-mapper Code/map2.sh \
	-reducer Code/reduce2.sh \
	-input 2014.out \
	-output final2014.out
`
to make sure the result are sorted and keys are distinct.

Similarly,<br />
`hjs \
	-files /scratch/YOUR-NETID/BigDataProject/Code \
	-mapper Code/map.sh \
	-reducer Code/reduce.sh \
	-input Datacleaned/yellow_2015.csv \
	-output temp2015.out
`
`hfs -getmerge temp2015.out 2015.out` <br />
`hfs -put 2015.out`<br />
`hjs \
	-D mapreduce.job.reduces=1 \
	-files /scratch/YOUR-NETID/BigDataProject/Code \
	-mapper Code/map2.sh \
	-reducer Code/reduce2.sh \
	-input 2015.out \
	-output final2015.out`
and<br />
`hjs \
	-files /scratch/YOUR-NETID/BigDataProject/Code \
	-mapper Code/map.sh \
	-reducer Code/reduce.sh \
	-input Datacleaned/yellow_2016.csv \
	-output temp2016.out
`
`hfs -getmerge temp2016.out 2016.out` <br />
`hfs -put 2016.out`<br />
`hjs \
	-D mapreduce.job.reduces=1 \
	-files /scratch/YOUR-NETID/BigDataProject/Code \
	-mapper Code/map2.sh \
	-reducer Code/reduce2.sh \
	-input 2016.out \
	-output final2016.out
`


#### To generate pickup location map, we use hadoop as data collector and matlab as drawer.Use:
`hjs \
	-files /scratch/YOUR-NETID/BigDataProject/Code \
	-mapper Code/map3.sh \
	-reducer Code/reduce3.sh \
	-input Datacleaned/yellow_2015.csv \
	-output drawdata.out`
And<br />
`hfs -getmerge drawdata.out drawdata1.out` <br />
`hfs -put drawdata1.out`<br />
`hjs \
	-D mapreduce.job.reduces=1 \
	-files /scratch/dz1108/BigDataProject/Code \
	-mapper Code/map2.sh \
	-reducer Code/reduce2.sh \
	-input drawdata1.out \
	-output draw.out`
`hfs -getmerge draw.out draw.out`
Then use the code in `MatlabCode`. We provide same data in the directory


## Progress Record
see ProgressRecord.md at root directory
