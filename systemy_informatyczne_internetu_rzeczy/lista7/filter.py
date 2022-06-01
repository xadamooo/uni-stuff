from tkinter import Y
from flask import Flask, request, render_template
import requests
import paho.mqtt.client as mqtt
from collections import defaultdict
import json
params = {}
app = Flask(__name__)
msg = {}
x = {}
y = {}
new_msg = {}
@app.route('/get-data',  methods=['GET', 'POST'])
def getParameters():
    if request.method == 'POST':
        parameters = request.form.to_dict()
        params['source'] = parameters['source']
        params['keys'] = parameters['keys']
        params['target'] = parameters['target']
    return parameters

@app.route('/data',  methods=['GET', 'POST'])
def getMessage():
    global y, new_msg
    mqttc = mqtt.Client()
    MQTT_HOST = "test.mosquitto.org"
    mqttc.connect(MQTT_HOST)
    if request.method == 'POST':
        y = request.form.to_dict()
        msg['dane'] = y
        new_keys = list(params['keys'].split(','))
        try:
            new_msg = {key : y[key] for key in new_keys}
            MQTT_MSG = json.dumps(new_msg)
            mqttc.publish(params['target'], MQTT_MSG)
            print(f'Message published to topic: {params["target"]}')
        except KeyError:
            x['info'] = 'nie ma takiego klucza'
            return x
        return y
    return new_msg


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=2000)