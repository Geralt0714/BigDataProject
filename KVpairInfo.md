# key Value Pair Documentation
Documentation for Key-Value pair in Hadoop MapReduce 

## Details
|Key  	|Value Range 	|Description|
|:-----:|:-------------:|:---------:|
|Meta data info|
|0-1|1					|count for data not worth mining|
|0-2|1					|total useful tuples counts|
|		Total Fee Distribution			|
|	1-1	|1				|	Total fee	in range [0,15)	|
|	1-2	|1				|	Total fee in range[15,40)		|
|	1-3	|1				|	Total fee in range[40,70)		|
|	1-4	|1				|	Tolal fee over 70		|
|1-5	|1				| Totle fee over 100
|		Tip willing 			|
|	2-1	|1				|	Pay by cash		|
|2-1-month|1|	Pay by cash each month|
|	2-2	|1				|	Pay by Credit card		|
|2-2-month|1|	Pay by Credit Card each month|
|	2-3	|	1			|	Not tipped		|
|	2-4	|	float			|	tip percentage count		|
|	2-5	|	1			|		tip time count	|
|2-5-1|float			| tip percent|
|2-6-1-hour|float	|tip percent by hour |
|2-6-2-hour|1		|tip time count by hour|
|2-7-1|float			|total Fare count|
|2-7-2|float			|total tip count|
|		location and time mining 							|
|3-1-1	|1| total pickup time count|
|3-1-2|1| pick up manhattan count|
|3-1-3|1| pick up in midtown count|
|3-2-hour |	1		| pick up at midtown hour distribution|
|3-3-hour|1				|leaving midtown|
|3-4-hour|1|	arriving midtown|
|3-5-hour|1				|leaving manhattan|
|3-6-hour|1|	arriving manhattan|
|midtown to LGA data mining	|
|4-hour	|	1	| pick up hour distribution|
|4-hour-1| float(in hours) 	| travel time consumption|
|4-hour-2|	float(in miles/hour)| travel speed count|
|4-hour-3|	1				| valid data count|
|midtown to JFK data mining	|
|5-hour	|	1	| pick up hour distribution|
|5-hour-1	| float(in hours) 	| travel time consumption|
|5-hour-2|	float(in miles/hour)| travel speed count|
|5-hour-3|	1				| valid data count|
|trip distance distribution|
|6-1|1|distance less than 1 mile|
|6-2|1|distance above 1 mile less than 2 miles|
|6-3|1|distance above 2 miles less than 4 miles|
|6-4|1|distance above 4 miles less than 6 miles|
|6-5|1|distance above 6 miles less than 8 miles|
|6-6|1|distance above 8 miles less than 10 miles|
|6-7|1|distance above 10 miles less than 14 miles|
|6-8|1|distance above 14 miles|



