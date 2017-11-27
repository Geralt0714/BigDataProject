# Data Info 

Green Taxi & Yellow Taxi Data Info, Data Cleaning Process Info

## Green Taxi Column Info 2016_01-2016_06

|Column Number	|Number in Code	|Column Name 	|Comments	|
|:-------------:|:-------------:|:-------------:|:---------:|
|1				|0		  		|VenderID		|			|
|2				|1				|Pickup_time	|			|
|3				|2				|Dropoff_time	|			|
|4				|3				|Store& Forward	|[1]		|
|5				|4				|RateCodeId		|[1]		|
|6				|5				|Pickup_long	|			|
|7				|6				|Pickup_lati	|			|
|8				|7				|Dropoff_long	|			|
|9				|8				|Dropoff_lati	|			|
|10				|9				|PassengerCount	|			|
|11				|10				|Trip_distance	|			|
|12				|11				|Fare			|			|
|13				|12				|Extra Fare		|			|
|14				|13				|MTA_tax		|[1]		|
|15				|14				|Tip			|			|
|16				|15				|Tolls			|			|
|17				|16				|Ehail_fee		|[1]		|
|18				|17				|ImprovementFee	|[1]			|
|19				|18				|TotalCharge	|			|
|20				|19				|PaymentType	|[2]		|
|21				|20				|Trip_trpe		|[1]			|

[1]Details in [Click Here](http://www.nyc.gov/html/tlc/downloads/pdf/data_dictionary_trip_records_green.pdf). We are not using these data because they are not related to this project, or they are the same (or void) in all data files.

[2]<br />
1 = Credit card <br />
2 = Cash <br />
3 = No charge <br />
4 = Dispute <br />
5 = Unknown <br />
6 = Voided trip <br />


## Green Taxi Column Info 2016_07-2016_12

|Column Number	|Number in Code	|Column Name 	|Comments	|
|:-------------:|:-------------:|:-------------:|:---------:|
|1				|0		  		|VenderID		|			|
|2				|1				|Pickup_time	|			|
|3				|2				|Dropoff_time	|			|
|4				|3				|Store& Forward	|[1]		|
|5				|4				|RateCodeId		|[1]		|
|6				|5				|PickupLocationID	|[2]			|
|7				|6				|DropoffLocationID	|[2]			|
|8				|7				|PassengerCount	|			|
|9				|8				|Trip_distance	|			|
|10				|9				|Fare			|			|
|11				|10				|Extra Fare		|			|
|12				|11				|MTA_tax		|[1]		|
|13				|12				|Tip			|			|
|14				|13				|Tolls			|			|
|15				|14				|Ehail_fee		|[1]		|
|16				|15				|ImprovementFee	|[1]			|
|17				|16				|TotalCharge	|			|
|18				|17				|PaymentType	|[3]		|
|19				|18				|Trip_trpe		|[1]			|

[1]Details in [Click Here](http://www.nyc.gov/html/tlc/downloads/pdf/data_dictionary_trip_records_green.pdf). We are not using these data because they are not related to this project, or they are the same (or void) in all data files.

[2]Details in taxi+zone+lookup.csv in root directory. Original Source:[Click Here](https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv)

[3]
1 = Credit card <br />
2 = Cash <br />
3 = No charge <br />
4 = Dispute <br />
5 = Unknown <br />
6 = Voided trip <br />


## Yellow Taxi Column Info 2016_01-2016-06

|Column Number	|Number in Code	|Column Name 	|Comments	|
|:-------------:|:-------------:|:-------------:|:---------:|
|1				|0		  		|VenderID		|			|
|2				|1				|Pickup_time	|			|
|3				|2				|Dropoff_time	|			|
|4				|3				|PassengerCount	|			|
|5				|4				|TripDistance	|			
|6				|5				|Pickup_long	|			|
|7				|6				|Pickup_lati	|			|
|8				|7				|RatecodeId		|[1]		|
|9				|8				|Store&Forward	|[1]		|
|10				|9				|Dropoff_long	|			|
|11				|10				|Dropoff_lati	|			|
|12				|11				|PaymentType	|[2]		|
|13				|12				|Fare			|			|
|14				|13				|Extra			|			|
|15				|14				|MTA_tax		|[1]		|
|16				|15				|Tip			|			|
|17				|16				|Tolls			|			|
|18				|17				|Improvement	|[1]		|
|19				|18				|TotalCharge	|			|

[1]Details in [Click Here](http://www.nyc.gov/html/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf). We are not using these data because they are not related to this project, or they are the same (or void) in all data files.

[2]Details in taxi+zone+lookup.csv in root directory. Original Source:[Click Here](https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv)

[2]<br />
1 = Credit card <br />
2 = Cash <br />
3 = No charge <br />
4 = Dispute <br />
5 = Unknown <br />
6 = Voided trip <br />

## Yellow Taxi Column Info 2016_07-2016-12

|Column Number	|Number in Code	|Column Name 	|Comments	|
|:-------------:|:-------------:|:-------------:|:---------:|
|1				|0		  		|VenderID		|			|
|2				|1				|Pickup_time	|			|
|3				|2				|Dropoff_time	|			|
|4				|3				|PassengerCount	|			|
|5				|4				|TripDistance	|			|
|6				|5				|RatecodeId		|[1]		|
|7				|6				|Store&Forward	|[1]		|
|8				|7				|PickupLocation	|[2]		|
|9				|8				|DropoffLocation|[2]		|
|10				|9				|PaymentType	|[3]		|
|11				|10				|Fare			|			|
|12				|11				|Extra			|			|
|13				|12				|MTA_tax		|[1]		|
|14				|13				|Tip			|			|
|15				|14				|Tolls			|			|
|16				|15				|Improvement	|[1]		|
|17				|16				|TotalCharge	|			|

[1]Details in [Click Here](http://www.nyc.gov/html/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf). We are not using these data because they are not related to this project, or they are the same (or void) in all data files.

[2]Details in taxi+zone+lookup.csv in root directory. Original Source:[Click Here](https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv)

[3]
1 = Credit card <br />
2 = Cash <br />
3 = No charge <br />
4 = Dispute <br />
5 = Unknown <br />
6 = Voided trip <br />

## Data Cleaning Process Info

For green taxi data, remove column (4,5,14,17,18,20), transform the pickup & dropoff location coordinates into borough name string. <br />
For yellow taxi data, remove column (6,7,13,16), transform pickup & dropoff location id into borough name string, re-arrange the order of columns.<br />

Remove rows with location coordinates of zeros


## Data Format After Cleaning

|Column Number |Number in Code   |Column Name   |Comments   |
|:-------------:|:-------------:|:-------------:|:---------:|
|1          |0          |VenderID      |        |
|2          |1          |Pickup_time   |        |
|3          |2          |Dropoff_time  |        |
|4          |3          |PickupLocation   |[1]        |
|5          |4          |DropoffLocation  |[1]        |
|6            |5          |PassengerCount   |        |
|7            |6            |Trip_distance |        |
|8            |7            |Fare       |        |
|9            |8            |Extra Fare    |        |
|10            |9            |Tip        |        |
|11            |10            |Tolls         |        |
|12            |11            |TotalCharge   |        |
|13            |12            |PaymentType   |[2]     |

[1]string with borough name
[2]
1 = Credit card <br />
2 = Cash <br />
3 = No charge <br />
4 = Dispute <br />
5 = Unknown <br />
6 = Voided trip <br />
