import paho.mqtt.client as mqtt
import requests


MQTT_HOST = "test.mosquitto.org"
MQTT_TOPIC = "/pcstat/cpu"


def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC)
    print('Connected...')


def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload)
    res = requests.post('http://127.0.0.1:5000/', data=msg.payload.decode('utf-8'))


mqttc = mqtt.Client()
mqttc.connect(MQTT_HOST)

mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.loop_forever()
