from flask import Flask, request, render_template
import requests
from matplotlib import pyplot as plt


data = {}
msg = {}
app = Flask(__name__)
filter_data = {}
y = {}

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
    global y
    if request.method == 'POST':
        x = 'Urzadzenie aktywne'
        y = request.form.to_dict()
        print(y)
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
    if request.method == 'POST':
        keys = request.form['keys']
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


@app.route('/visualize')
def chartTest():
    chart_data = []
    chart_data.append(y['Turbidity'])
    plt.plot(chart_data)   
    plt.savefig('/static/images/new_plot.png')
    return render_template('visualize.html', name = 'new_plot', url ='/static/images/new_plot.png')


@app.route('/aggregate',  methods=['GET', 'POST'])
def getaggr():
    return render_template('aggr.html')


@app.route('/filtering',  methods=['GET', 'POST'])
def getfilter():
    return render_template('filter.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4000)
