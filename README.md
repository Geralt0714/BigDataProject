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

In this process, it will create directory ./Data and ./Datacleaned to store the raw data and data files after cleaning<br />
Those data files are stored locally, not in HDFS<br />

For more data cleaning details, see DataInfo.md

## Part II: Data Analysis

#### Push data file into HDFS
`hfs -put Datacleaned/.`
This could take a moment <br />
After pushing into hdfs, you can use `hfs -ls Datacleaned` to see the loaded data files<br />

## Bonus: Data Exploration
*\<TODO\>*

## Progress Record
see ProgressRecord.md at root directory
