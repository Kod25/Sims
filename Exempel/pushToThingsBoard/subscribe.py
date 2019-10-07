import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random

THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'wHNpQWFoo07alXNHSOAl'

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    # Subscrizbing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("v1/device/me/telemetry/+")


def on_message(client, userdata, msg):
    print("topic: " + msg.topic)
    print("Message: " + str(msg.payload))

    data = json.loads(msg.payload)
    print("decoded: " + data)

def on_log(client, userdata, level, buf):
    print("log: ", buf)

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log
# Set access token
client.username_pw_set(ACCESS_TOKEN)


# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_forever()




#client.loop_stop()