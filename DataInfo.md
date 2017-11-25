# Data Info 

Green Taxi & Yellow Taxi Data Info

## Green Taxi Column Info

|Column Number	|Number in Code	|Column Name 	|Comments	|
|:-------------:|:-------------:|:-------------:|:---------:|
|1				|0		  		|VenderID		|			|
|2				|1				|Pickup_time	|			|
|3				|2				|Dropoff_time	|			|
|4				|3				|Store& Forward	|[1]		|
|5				|4				|RateCodeId		|[1]		|
|6				|5				|Pickup_Long	|			|
|7				|6				|Pickup_lati	|			|
|8				|7				|Dropoff_long	|			|
|9				|8				|Dropoff_lati	|			|
|10				|9				|PassengerCount	|			|
|11				|10				|Trip_distance	|			|
|12				|11				|Fare			|			|
|13				|12				|Extra Fare		|			|
|14				|13				|MTA_tax		|			|
|15				|14				|Tip			|			|
|16				|15				|Tolls			|			|
|17				|16				|Ehail_fee		|[1]		|
|18				|17				|ImprovementFee	|			|
|19				|18				|TotalCharge	|			|
|20				|19				|PaymentType	|[2]		|
|21				|20				|Trip_trpe		|			|

[1]Details in [Click Here](http://www.nyc.gov/html/tlc/downloads/pdf/data_dictionary_trip_records_green.pdf). We are not using these data because they are not related to this project, or they are the same (or void) in all data files.

[2]1 = Credit card 
   2 = Cash
   3 = No charge 
   4 = Dispute
   5 = Unknown
   6 = Voided trip


## Yellow Taxi Column Info

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

[3]1 = Credit card 
   2 = Cash
   3 = No charge 
   4 = Dispute
   5 = Unknown
   6 = Voided trip