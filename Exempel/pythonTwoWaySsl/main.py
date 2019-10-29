#
# Copyright © 2016-2019 The Thingsboard Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random
import ssl, socket


def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))



# The callback for when the client receives a CONNACK response from the server.
THINGSBOARD_HOST = '40.113.77.241'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL = 5

sensor_data = {'analog1': 0, 'analog2': 0, 'analog3': 0, 'digital1': 0, 'digital2': 0, 'digital3': 0, 'digital4': 0,
               'digital5': 0}

next_reading = time.time()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(ca_certs="mqttserver.pub.pem",
               certfile="mqttclient.nopass.pem",
               keyfile="mqttclient.p12",
               cert_reqs=ssl.CERT_REQUIRED,
               tls_version=ssl.PROTOCOL_TLSv1_2,
               ciphers=None)

client.tls_insecure_set(False)
client.connect(socket.gethostname(), 8883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
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

        sensor_data['analog1'] = flow_in
        sensor_data['analog2'] = volume
        sensor_data['analog3'] = flow_out
        sensor_data['digital1'] = alarm_full
        sensor_data['digital2'] = 0
        sensor_data['digital3'] = 0
        sensor_data['digital4'] = alarm_empty
        sensor_data['digital5'] = engine
        print(sensor_data)

        counter = counter + 1

        # Sending humidity and temperature data to ThingsBoard
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass



client.loop_stop()
