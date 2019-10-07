import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random

THINGSBOARD_HOST = 'demo.thingsboard.io'
#'127.0.0.1'
ACCESS_TOKEN = 'wHNpQWFoo07alXNHSOAl'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=5
#hej
sensor_data = {'temperature': 0, 'pH': 0}

next_reading = time.time()

client = mqtt.Client()

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()

try:
    while True:
        #pH = random.randint(0,100)
        #temperature = random.randint(-10, 40)
        #pH = round(pH, 2)
        #temperature = round(temperature, 2)
        #print(u"temperature: {:g}\u00b0C, pH: {:g}".format(temperature, pH))
        #sensor_data['temperature'] = temperature
        #sensor_data['pH'] = pH

        pH = random.uniform(0, 14)

        flow = random.uniform(1.1, 1.2)

        temperature = random.uniform(17.8, 18)

        sensor_data['temperature'] = temperature
        sensor_data['pH'] = pH
        sensor_data['flow'] = flow



        # Sending humidity and temperature data to ThingsBoard
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()