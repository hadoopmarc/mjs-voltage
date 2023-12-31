# HiveMQ free secure private MQTT broker

A free secure private cloud-based MQTT broker can be instantiated at: [https://www.hivemq.com/downloads](https://www.hivemq.com/downloads). It is limited to 100 connected devices, but an unlimited open source docker version is available that can be hosted elsewhere, if needed.

Use of the [public cloud-based HiveMQ broker](https://www.hivemq.com/public-mqtt-broker/) is not advised, because this would expose tasmota devices to the MQTT cmd/# topics.

Getting MQTT client tools working with the HiveMQ cloud broker is a bit confusing, so see some recipes below. The recipes assume that HIVEMQ_URL, HIVEMQ_USER and HIVEMQ_PWD environment variable are set. You can put these in a .env file in the project root and activate them in a terminal, using:

```bash
$ . bin/setenv.sh
```

## MQTTK

This GUI-based tool is the easiest to get working, because it allows to store configurations and quickly try out a lot of permutations of configuration options. Working with it showed that the private cloud-based HiveMQ broker uses certificates from a public CA, so no certificate of the private broker needs to be downloaded to establish a TLS connection. Even better: HiveMQ uses a certificate from Let's Encrypt which is supported by the tasmota software to be installed in the smart plugs.

```bash
$ python3 -m pip install mqttk
$ mqttk
```
| | |
|--- |--- |
|Configured public domain                       |broker.hivemq.com|
|MQTT version                                   |3.3.1 (5.0 does not connect)|
|Port 1883, no ssl                              |publish and subscribe works!|
|Port 8883, ssl with option ca-signed server    |publish and subscribe works!|

<br>

| | |
|--- |--- |
|Configured private domain                      |$HIVEMQ_FQDN|
|User/password                                  |$HIVEMQ_USER/$HIVEMQ_PWD|
|MQTT version                                   |3.3.1 (5.0 does not connect)|
|Port 8883, ssl with option ca-signed server    |publish and subscribe works!|

The mqttk tool is also interesting because it depends on the paho-mqtt python library, so it serves as an example how to configure custom python clients.


## MQTTX

See [https://mqttx.app/downloads](https://mqttx.app/downloads)

```bash
$ sudo apt install ./MQTTX_1.9.4_amd64.deb
```

This simply works with the HiveMQ private domain, username and password, specifying secure TLS with a CA-signed certificate.


## Debian Mosquitto clients

Error messages from these clients are missing or unhelpful, but below commands work:

```bash
$ sudo apt install mosquitto-clients

$ mosquitto_sub -h $HIVEMQ_FQDN -p 8883 -u $HIVEMQ_USER -P $HIVEMQ_PWD --cafile /etc/ssl/certs/ca-certificates.crt -t tasmota

$ mosquitto_pub -h $HIVEMQ_FQDN -p 8883 -u $HIVEMQ_USER -P $HIVEMQ_PWD --cafile /etc/ssl/certs/ca-certificates.crt -t tasmota -m 'From mosquitto'
```

## HiveMQ CLI tool

This is a java based tool from HiveMQ itself. Java has its own way for getting public CA certificates, so --cafile /etc/ssl/certs/ca-certificates.crt does not do the trick here. Instead, the https://www.hivemq.com/ server.pem certificate was downloaded using the browser and specified instead (but probably it is also possible to use the --ts and --tspw options to use the system java truststore).

The HiveMQ CLI tool can be downloaded from [https://www.hivemq.com/blog/mqtt-cli/](https://www.hivemq.com/blog/mqtt-cli/)

```bash
$ sudo apt install ./mqtt-cli-4.17.0.deb

$ mqtt sub -h $HIVEMQ_FQDN -p 8883 -u $HIVEMQ_USER -pw $HIVEMQ_PWD --cafile dev/server.pem -V 3 -t tasmota

$ mqtt pub -h $HIVEMQ_FQDN -p 8883 -u $HIVEMQ_USER -pw $HIVEMQ_PWD --cafile dev/server.pem -V 3 -t tasmota -m 'From mosquitto'
```

# Local MQTT broker

If you want to try out things before setting up a private cloud-based MQTT broker, you can start with a MQTT broker on a local network. On debian based systems like Ubuntu a local MQTT broker can be installed with:

```bash
$ sudo apt-get install mosquitto
```

By default it runs without TLS on port 1883.