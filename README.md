# ThingSpeakPy
Upload data to [ThingSpeak](https://thingspeak.com/) in Python (socket level).

## Getting Started

### Instructions:

#### Clone

First clone this repo:

```shell
"$ git clone https://github.com/ArielBarros/ThingSpeakPy.git"
```

#### Execute

In the directory you have downloaded, run the following script, some parameters are required: key and data to be sent. For example:

```shell
"$ python ThingSpeak_pub.py -k XFIAM10CT78X2NRF 2 5 10"
```
It will send: 
* field1 = 2
* field2 = 5
* field3 = 10 

For get channel feed/field, run the following script, some parameters are required: read apikey, id channel, fields and number of results. For example:

```shell
"$ python ThingSpeak_recv.py -i 289885 -k RUOPEE8SJH9FPL4W -f 0 -r 0
```
For field equals to 0, will return all the fields. For results equals to 0, will return all data registered in the specific field.

The channel used in this examples that corresponding to __XFIAM10CT78X2NRF__ key, __RUOPEE8SJH9FPL4W__ read key and __289885__ id channel is [This Channel](https://thingspeak.com/channels/289885). 

For send data to your own channel, change the parameters.
## Author

[__ArielBarros__](https://github.com/ArielBarros)
