# ShellyPlusPlusS_Logger.py

import time
import logging
import re
import json
from typing import NamedTuple
import paho.mqtt.client as mqtt
import os

MQTT_SERVER = os.environ['MQTT_Server']
MQTT_PORT = 8883
MQTT_USER = os.environ['MQTT_USER']
MQTT_PASSWORD = os.environ['MQTT_PASSWORD']
MQTT_TOPIC = 'shellyplusplugs/events/rpc'



