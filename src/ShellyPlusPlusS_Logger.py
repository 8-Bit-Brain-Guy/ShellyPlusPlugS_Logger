# ShellyPlusPlusS_Logger.py

import time
import logging
import re
import json
from typing import NamedTuple
import paho.mqtt.client as mqtt
import os


# Set this variables in Linux using: export MQTT_Server=12678467823
# Show them using:                   echo $MQTT_Server

MQTT_SERVER = os.environ['MQTT_SERVER']
MQTT_PORT = 8883
MQTT_USER = os.environ['MQTT_USER']
MQTT_PASSWORD = os.environ['MQTT_PASSWORD']
MQTT_TOPIC = 'shellyplusplugs/events/rpc'

print("MQTT_SERVER: %s" %MQTT_SERVER)
print("MQTT_USER:   %s" %MQTT_USER)



