import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random

THINGSBOARD_HOST = 'thingsboard-af.northeurope.cloudapp.azure.com'

ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAA'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=5

sensor_data = {'analog1': 0, 'analog2': 0, 'analog3': 0, 'digital1': 0, 'digital2': 0, 'digital3': 0}

next_reading = time.time()

client = mqtt.Client()

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()

volume = 0

counter = 0

try:
    while True:
        alarm_full = 0
        alarm_empty = 0

        flow_out = random.uniform(2.1, 3.2)

        flow_in = random.uniform(2.5, 3.5)

        if volume > 10:
            volume = 0

        if volume == 0:
            volume = random.uniform(0, 3)

        volume = volume + random.uniform(0.1, 1.5)

        if volume < 3:
            alarm_empty = 1

        if 11.5 > volume > 8:
            alarm_full = 1

        if counter % 10 == 0:
            engine = 1
        else:
            engine = 0

        sensor_data['analog1'] = volume
        sensor_data['analog2'] = flow_in
        sensor_data['analog3'] = flow_out
        sensor_data['digital1'] = alarm_full
        sensor_data['digital2'] = alarm_empty
        sensor_data['digital3'] = engine

        print(sensor_data)

        counter = counter + 1

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