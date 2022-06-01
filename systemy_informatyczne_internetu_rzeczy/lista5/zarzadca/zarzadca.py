from flask import Flask, request, render_template
import requests
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np

data = {}
msg = {}
app = Flask(__name__)
filter_data = {}
chart_list = [0]
i = 0
fig = go.FigureWidget()
fig.add_scatter()


@app.route('/',  methods=['GET', 'POST'])
def paramsTopic():
    if request.method == 'POST':
        topic = request.form.to_dict()
        data['topic'] = topic
        return topic
    return data


def paramsProt():
    if request.method == 'POST':
        prot = request.form.to_dict()
        data['prot'] = prot
        return prot
    return data


def paramsFreq():
    if request.method == 'POST':
        freq = request.form.to_dict()
        data['freq'] = freq
        return freq
    return data


def paramsFile():
    if request.method == 'POST':
        file = request.form.to_dict()
        data['file'] = file
        return file
    return data


@app.route('/data',  methods=['GET', 'POST'])
def getMessage():
    global i, fig
    if request.method == 'POST':
        x = 'Urzadzenie aktywne'
        y = request.form.to_dict()
        chart_list.append(float(y[filter_data['keys']]))
        fig.data[0].y = chart_list[:i]
        i = i + 1 
        msg['status'] = x
        msg['dane'] = y
        r = requests.post('http://127.0.0.1:2000/data', data=msg['dane'])
        return x, y
    return msg


@app.route('/get-aggtime', methods=['GET', 'POST'])
def aggtime():
    if request.method == 'POST':
        aggtime = request.form['aggtime']
        data['aggtime'] = aggtime
        r = requests.post('http://127.0.0.1:3000/aggtime', data=data)
        return render_template('aggr.html')
    return data


@app.route('/get-source', methods=['GET', 'POST'])
def source():
    if request.method == 'POST':
        source = request.form['source']
        filter_data['source'] = source
        r = requests.post('http://127.0.0.1:2000/get-data', data=filter_data)
        return render_template('filter.html')
    return filter_data


@app.route('/get-keys', methods=['GET', 'POST'])
def keys():
    global fig, chart_list
    if request.method == 'POST':
        keys = request.form['keys']
        try:
            if keys != filter_data['keys']:
                chart_list = [0]
                filter_data['keys'] = keys
        except KeyError:
            filter_data['keys'] = keys
        r = requests.post('http://127.0.0.1:2000/get-data', data=filter_data)
        return render_template('filter.html')
    return filter_data


@app.route('/get-target', methods=['GET', 'POST'])
def target():
    if request.method == 'POST':
        target = request.form['target']
        filter_data['target'] = target
        r = requests.post('http://127.0.0.1:2000/get-data', data=filter_data)
        return render_template('filter.html')
    return filter_data


@app.route('/aggregate',  methods=['GET', 'POST'])
def getaggr():
    return render_template('aggr.html')


@app.route('/visualizeconfig',  methods=['GET', 'POST'])
def getfilter():
    return render_template('filter.html')


@app.route('/visualize')
def notdash():
    fig.update_layout(
    height=800,
    title_text = filter_data['keys'])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('visualize.html', graphJSON=graphJSON)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4000)
