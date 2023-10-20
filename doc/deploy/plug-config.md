# Configuration of a smart plug





MQTT Tasmota:           https://tasmota.github.io/docs/MQTT/
MQTT commands Tasmota:  https://tasmota.github.io/docs/Commands/#mqtt

Terminal logging of MQTT messages from Athom_M1 (with default TelePeriod 300):

marc@antecmarc:~$ mosquitto_sub -h localhost -t +/#

Online
{"ip":"192.168.2.71","dn":"Tasmota","fn":["Tasmota",null,null,null,null,null,null,null],"hn":"tasmota-F17F56-8022","mac":"E09806F17F56","md":"Athom Plug V2","ty":0,"if":0,"ofln":"Offline","onln":"Online","state":["OFF","ON","TOGGLE","HOLD"],"sw":"10.1.0","t":"tasmota_F17F56","ft":"%prefix%/%topic%/","tp":["cmnd","stat","tele"],"rl":[1,0,0,0,0,0,0,0],"swc":[-1,-1,-1,-1,-1,-1,-1,-1],"swn":[null,null,null,null,null,null,null,null],"btn":[0,0,0,0,0,0,0,0],"so":{"4":0,"11":0,"13":0,"17":0,"20":0,"30":0,"68":0,"73":0,"82":0,"114":0,"117":0},"lk":0,"lt_st":0,"sho":[0,0,0,0],"ver":1}
{"sn":{"Time":"2023-06-24T08:39:31","ENERGY":{"TotalStartTime":"2023-06-24T08:32:22","Total":0.000,"Yesterday":0.000,"Today":0.000,"Power": 0,"ApparentPower": 0,"ReactivePower": 0,"Factor":0.00,"Voltage":233,"Current":0.000}},"ver":1}

{"Time":"2023-06-24T09:19:26","Uptime":"0T00:40:09","UptimeSec":2409,"Heap":26,"SleepMode":"Dynamic","Sleep":50,"LoadAvg":19,"MqttCount":1,"POWER":"ON","Wifi":{"AP":1,"SSId":"Beneden","BSSId":"2C:91:AB:45:EE:E1","Channel":1,"Mode":"11n","RSSI":92,"Signal":-54,"LinkCount":1,"Downtime":"0T00:00:03"}}
{"Time":"2023-06-24T09:19:26","ENERGY":{"TotalStartTime":"2023-06-24T08:32:22","Total":0.001,"Yesterday":0.000,"Today":0.001,"Period": 0,"Power": 0,"ApparentPower": 0,"ReactivePower": 0,"Factor":0.00,"Voltage":234,"Current":0.000}}

{"Time":"2023-06-24T09:24:26","Uptime":"0T00:45:09","UptimeSec":2709,"Heap":26,"SleepMode":"Dynamic","Sleep":50,"LoadAvg":19,"MqttCount":1,"POWER":"ON","Wifi":{"AP":1,"SSId":"Beneden","BSSId":"2C:91:AB:45:EE:E1","Channel":1,"Mode":"11n","RSSI":90,"Signal":-55,"LinkCount":1,"Downtime":"0T00:00:03"}}
{"Time":"2023-06-24T09:24:26","ENERGY":{"TotalStartTime":"2023-06-24T08:32:22","Total":0.001,"Yesterday":0.000,"Today":0.001,"Period": 0,"Power": 1,"ApparentPower": 9,"ReactivePower": 9,"Factor":0.08,"Voltage":233,"Current":0.039}}

{"Time":"2023-06-24T09:29:26","Uptime":"0T00:50:09","UptimeSec":3009,"Heap":26,"SleepMode":"Dynamic","Sleep":50,"LoadAvg":19,"MqttCount":1,"POWER":"ON","Wifi":{"AP":1,"SSId":"Beneden","BSSId":"2C:91:AB:45:EE:E1","Channel":1,"Mode":"11n","RSSI":94,"Signal":-53,"LinkCount":1,"Downtime":"0T00:00:03"}}
{"Time":"2023-06-24T09:29:26","ENERGY":{"TotalStartTime":"2023-06-24T08:32:22","Total":0.001,"Yesterday":0.000,"Today":0.001,"Period": 0,"Power": 0,"ApparentPower": 0,"ReactivePower": 0,"Factor":0.00,"Voltage":233,"Current":0.000}}

{"Time":"2023-06-24T09:34:26","Uptime":"0T00:55:09","UptimeSec":3309,"Heap":26,"SleepMode":"Dynamic","Sleep":50,"LoadAvg":19,"MqttCount":1,"POWER":"ON","Wifi":{"AP":1,"SSId":"Beneden","BSSId":"2C:91:AB:45:EE:E1","Channel":1,"Mode":"11n","RSSI":92,"Signal":-54,"LinkCount":1,"Downtime":"0T00:00:03"}}
{"Time":"2023-06-24T09:34:26","ENERGY":{"TotalStartTime":"2023-06-24T08:32:22","Total":0.001,"Yesterday":0.000,"Today":0.001,"Period": 0,"Power": 0,"ApparentPower": 0,"ReactivePower": 0,"Factor":0.00,"Voltage":232,"Current":0.000}}

{"Time":"2023-06-24T09:39:26","Uptime":"0T01:00:09","UptimeSec":3609,"Heap":26,"SleepMode":"Dynamic","Sleep":50,"LoadAvg":19,"MqttCount":1,"POWER":"ON","Wifi":{"AP":1,"SSId":"Beneden","BSSId":"2C:91:AB:45:EE:E1","Channel":1,"Mode":"11n","RSSI":92,"Signal":-54,"LinkCount":1,"Downtime":"0T00:00:03"}}
{"Time":"2023-06-24T09:39:26","ENERGY":{"TotalStartTime":"2023-06-24T08:32:22","Total":0.001,"Yesterday":0.000,"Today":0.001,"Period": 0,"Power": 0,"ApparentPower": 0,"ReactivePower": 0,"Factor":0.00,"Voltage":233,"Current":0.000}}

{"Time":"2023-06-24T09:44:26","Uptime":"0T01:05:09","UptimeSec":3909,"Heap":26,"SleepMode":"Dynamic","Sleep":50,"LoadAvg":19,"MqttCount":1,"POWER":"ON","Wifi":{"AP":1,"SSId":"Beneden","BSSId":"2C:91:AB:45:EE:E1","Channel":1,"Mode":"11n","RSSI":92,"Signal":-54,"LinkCount":1,"Downtime":"0T00:00:03"}}
{"Time":"2023-06-24T09:44:26","ENERGY":{"TotalStartTime":"2023-06-24T08:32:22","Total":0.001,"Yesterday":0.000,"Today":0.001,"Period": 0,"Power": 0,"ApparentPower": 0,"ReactivePower": 0,"Factor":0.00,"Voltage":232,"Current":0.000}}



