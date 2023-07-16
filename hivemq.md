$ . setenv.sh

This will not work yet...

$ mosquitto_pub -h 593d7131864a4e60a19dde655555b6f2.s2.eu.hivemq.cloud -p 8883 -u $HIVEMQ_USER -P $HIVEMQ_PWD -t voltage/tasmota -m 'From mosquitto'

$ mosquitto_sub -h 593d7131864a4e60a19dde655555b6f2.s2.eu.hivemq.cloud -p 8883 -u $HIVEMQ_USER -P $HIVEMQ_PWD -t tasmota


With hivemq mqtt cli tool:

$ mqtt shell
con -h 593d7131864a4e60a19dde655555b6f2.s2.eu.hivemq.cloud -p 8883 -u $HIVEMQ_USER -pw $HIVEMQ_PWD
--ca-cert /etc/ssl/certs/ca-certificates.crt

--ca-cert is an improvement. Now: Unable to connect. Reason: 'No trusted certificate found'

$ mqtt shell
con -h 593d7131864a4e60a19dde655555b6f2.s2.eu.hivemq.cloud -p 8883 -u $HIVEMQ_USER -pw $HIVEMQ_PWD
--ca-cert ./server.pem

--ca-cert is an improvement. Now: Unable to connect. Reason: 'CONNECT failed as CONNACK contained an Error Code: NOT_AUTHORIZED.'


2023-07-16
New attempts with the mqttk tool and the various HiveMQ servers.

$ python3 -m pip install mqttk
$ mqttk

Configured url:                                 broker.hivemq.com
MQTT version:                                   3.3.1 (5.0 does not connect)
Port 1883, no ssl:                              publish and subscribe works!
Port 8883, ssl with option ca-signed server:    publish and subscribe works!

Configured url:                                 broker.hivemq.com
User/password as in .env
MQTT version:                                   3.3.1 (5.0 does not connect)
Port 8883, ssl with option ca-signed server:    publish and subscribe works!

This is good news, because mqttk depends on paho-mqtt


And this one works too:
https://mqttx.app/downloads
This simply works with the HiveMQ private url, username and password, specifying secure TLS with a CA-signed certificate.
