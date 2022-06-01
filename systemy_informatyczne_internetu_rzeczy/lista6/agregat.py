from re import U
from flask import Flask, request
import time

database1 = {}
database2 = {}
database3 = {}
database4 = {}
database5 = {}
database = {}
y1 = [0]
y2 = [0]
y3 = [0]
y4 = [0]
y5 = [0]
app = Flask(__name__)
data = {}
aggtime = 2


@app.route('/agg',  methods=['GET', 'POST'])
def agg():
    global aggtime, y1, y2, y3, y4 ,y5
    del y1[0:len(y1) - int(aggtime)]
    del y2[0:len(y2) - int(aggtime)]
    del y3[0:len(y3) - int(aggtime)]
    del y4[0:len(y4) - int(aggtime)]
    del y4[0:len(y5) - int(aggtime)]
    database1['avgtemp'] = sum(y1) / len(y1)
    database2['avg_active_vehicles'] = sum(y2) / len(y2)
    database3['max voltage'] = sum(y3) / len(y3)
    database4['avg fees in k$'] = sum(y4) / len(y4)
    database5['data'] = sum(y5) / len(y5)
    database['database1'] = database1
    database['database2'] = database2
    database['database3'] = database3
    database['database4'] = database4
    database['database5'] = database5
    return database


@app.route('/aggtime',  methods=['GET', 'POST'])
def paramsAggtime():
    global aggtime, y1
    if request.method == 'POST':
        aggtime = request.form.to_dict()
        data['aggtime'] = aggtime['aggtime']
        aggtime = aggtime['aggtime']
        return aggtime
    return data


@app.route('/database1',  methods=['GET', 'POST'])
def getMessage1():
    global aggtime, y2
    if request.method == 'POST':
        x = request.form
        try:
            y1.append(float(x["Water Temperature"]))
            database1['avgtemp'] = sum(y1) / len(y1)
            return x
        except KeyError:
            return x
    return database1


@app.route('/database2',  methods=['GET', 'POST'])
def getMessage2():
    global aggtime
    if request.method == 'POST':
        z = request.form
        try:
            y2.append(float(z["active_vehicles"]))
            database2['avg_active_vehicles'] = sum(y2) / len(y2)
            return z
        except KeyError:
            return z
    return database2


@app.route('/database3',  methods=['GET', 'POST'])
def getMessage3():
    global aggtime
    if request.method == 'POST':
        p = request.form
        try:
            y3.append(float(p["Voltage"]))
            database3['max voltage'] = max(y3)
            return p
        except KeyError:
            return p
    return database3

@app.route('/database4',  methods=['GET', 'POST'])
def getMessage4():
    global aggtime
    if request.method == 'POST':
        l = request.form
        try:
            fee = l["Tuition and fees"]
            fee = fee[1:-1]
            fee = fee.replace(',', '.')
            y4.append(float(fee))
            database4['avg fees in k$'] = round(sum(y4) / len(y4), 3)
            return l
        except KeyError:
            return l
    return database4

@app.route('/database5',  methods=['GET', 'POST'])
def getMessage5():
    global aggtime
    if request.method == 'POST':
        g = request.form
        try:
            database5['data'] = g
            database5['stat'] = 'no data to calculate any statistic'
            return g
        except KeyError:
            return g
    return database5


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)