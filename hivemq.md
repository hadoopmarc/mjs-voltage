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