import csv
import time
import requests
import json
import paho.mqtt.client as mqtt


'wstepne parametry'
freq = 2
where_to_send = 'http://127.0.0.1:4000/data'
topic ='/database/1'
y = 'mqtt'
fp = "D:\\PWR\\Visual Studio\\systemy_informatyczne_internetu_rzeczy\\lista5\\datasets\\data1.csv"
prev = 0
restart = True


while restart:
    input_file = csv.DictReader(open(fp))
    header = next(input_file)
    for row in input_file:
        try:
            file_path = requests.get('http://127.0.0.1:4000/').json()
        except KeyError:
            pass
        else:
            file_path = file_path['topic']['file']
            if fp != file_path:
                fp = file_path
                break
        try:
            x = requests.get('http://127.0.0.1:4000/').json()
        except KeyError:
            x = y
        else:
            x = x['topic']
        if x['prot'] == 'http':
            r = requests.post(where_to_send, data=row)
            print('Data passed to server...')
            try:
                frequency = requests.get('http://127.0.0.1:4000/').json()
            except KeyError:
                frequency = freq
            else:
                frequency = frequency['topic']
            time.sleep(int(frequency['freq']))

        if x['prot'] == 'mqtt':
            mqttc = mqtt.Client()
            MQTT_HOST = "test.mosquitto.org"
            mqttc.connect(MQTT_HOST)
            try:
                mqtt_topic = requests.get('http://127.0.0.1:4000/').json()
            except KeyError:
                mqtt_topic = topic
            else:
                mqtt_topic = mqtt_topic['topic']
            MQTT_MSG = json.dumps(row)
            mqttc.publish(mqtt_topic, MQTT_MSG)
            print('Message published...')
            try:
                frequency = requests.get('http://127.0.0.1:4000/').json()
            except KeyError:
                frequency = freq
            time.sleep(int(frequency['freq']))
