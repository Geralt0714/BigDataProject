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
|		pick up mining 							|
|3-1-1	|1| total pickup time count|
|3-1-2|1| pick up manhattan count|
|    3-2-hour |	1		| pick up at midtown hour distribution|
|	4-1-1	|1				|pick up at midtown count|
|4-1-2	|1				|pick up not at midtown count|
|4-2-hour|1				|leaving midtown|
|4-3-hour|1|	arriving midtown|
|midtown to JFK data mining	|
|5-hour	|	1	| pick up hour distribution|
|5-hour-1	| float(in hours) 	| travel time consumption|
|5-hour-2|	float(in miles/hour)| travel speed count|
|5-hour-3|	1				| valid data count|

