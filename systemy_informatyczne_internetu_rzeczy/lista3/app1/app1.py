import paho.mqtt.client as mqtt
import json
import datetime
import psutil
import time

MQTT_HOST = "test.mosquitto.org"
MQTT_TOPIC = "/pcstat/cpu"


def get_stats():
    cpu = psutil.cpu_percent()
    time1 = datetime.datetime.now()
    message = {'cpu usage[%]': cpu, 'time': str(time1)}
    return message


mqttc = mqtt.Client()
mqttc.connect(MQTT_HOST)
while True:
    MQTT_MSG = json.dumps(get_stats())
    print(MQTT_MSG)
    mqttc.publish(MQTT_TOPIC, MQTT_MSG)
    time.sleep(1)
