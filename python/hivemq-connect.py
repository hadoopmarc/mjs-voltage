
# This script reads the voltage topic from the mjs-voltage HiveMQ broker

import os
import ssl
import sys

import dotenv
import paho.mqtt.client as mqtt


host = "593d7131864a4e60a19dde655555b6f2.s2.eu.hivemq.cloud"  # Free mjs-voltage cluster
port = 8883
keepalive = 60
topic = 'voltage'

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
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host, port, keepalive)
    print('After connect', type(os.getenv('HIVEMQ_USER')))
    client.username_pw_set(os.getenv('HIVEMQ_USER'), os.getenv('HIVEMQ_PWD'))
    print('After pw')
    # client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
    client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
    print('After tls')
    client.subscribe(topic, qos=0)
    print('After sub')
    
    while True:
        client.loop()


if __name__ == "__main__":
    main()

