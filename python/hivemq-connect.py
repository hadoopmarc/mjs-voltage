
# This script reads the voltage topic from the mjs-voltage HiveMQ broker

import os
import ssl
import sys

import dotenv
import paho.mqtt.client as mqtt


port = 8883
keepalive = 60
topic_pattern = 'voltage/#'

# Local .env file should provide HIVEMQ_FQDN, HIVEMQ_USER and HIVEMQ_PWD env variables
dotenv.load_dotenv()



def on_connect(client, userdata, flags, rc):
    print("Connection returned result: ", rc)


def on_message(client, userdata, message):
    print('----------------------')
    print('topic: %s',  message.topic)
    print('payload: %s', message.payload)
    print('qos: %d', message.qos)
    print(message.payload.decode("utf-8"))


def main():
    # See https://github.com/matesh/mqttk/blob/master/mqttk/MQTT_manager.py
    # for the paho calls used by the mqttk command line client
    client = mqtt.Client(
        'device_id',
        clean_session=True,
        userdata=None,
        protocol=mqtt.MQTTv311,
        transport="tcp")
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(os.getenv('HIVEMQ_USER'), os.getenv('HIVEMQ_PWD'))
    print('After pw')
    client.tls_set(
        ca_certs=None,
        certfile=None,
        keyfile=None,
        cert_reqs=ssl.CERT_REQUIRED,
        tls_version=ssl.PROTOCOL_TLS,
        ciphers=None,
        keyfile_password=None)
    print('After tls')
    client.connect(os.getenv('HIVEMQ_FQDN'), port, keepalive)
    print('After connect')
    client.subscribe(topic_pattern, qos=0)
    print('After sub')
    
    while True:
        client.loop()


if __name__ == "__main__":
    main()

