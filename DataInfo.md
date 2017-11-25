# Data Info 

Green Cab Data Info

## Column Info

|Column Number	|Number in Code	|Column Name 	|Comments	|
|:-------------:|:-------------:|:-------------:|:---------:|
|1				|0		  		|VenderID		|			|
|2				|1				|Pickup_time	|			|
|3				|2				|Dropoff_time	|			|
|4				|3				|Store& Forward	|*			|
|5				|4				|RateCodeId		|*			|
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
|17				|16				|Ehail_fee		|*			|
|18				|17				|ImprovementFee	|			|
|19				|18				|TotalCharge	|			|
|20				|19				|PaymentType	|**			|
|21				|20				|Trip_trpe		|			|

* Details in [Click Here](http://www.nyc.gov/html/tlc/downloads/pdf/data_dictionary_trip_records_green.pdf). We are not using these data because they are not related to this project or, they are the same in all data files.

**1 = Credit card 
  2 = Cash
  3 = No charge 
  4 = Dispute
  5 = Unknown
  6 = Voided trip