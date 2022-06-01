from flask import Flask, request, render_template
import requests

data = {}
app = Flask(__name__)


@app.route('/',  methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/get-topic', methods=['GET', 'POST'])
def topic():
    if request.method == 'POST':
        topic = request.form['topic']
        data['topic'] = topic
        r = requests.post('http://127.0.0.1:4000/', data=data)
        return render_template('index.html')
    return data


@app.route('/get-freq', methods=['GET', 'POST'])
def freq():
    if request.method == 'POST':
        freq = request.form['freq']
        data['freq'] = freq
        r = requests.post('http://127.0.0.1:4000/', data=data)
        return render_template('index.html')
    return data


@app.route('/get-prot', methods=['GET', 'POST'])
def prot():
    if request.method == 'POST':
        prot = request.form['prot']
        data['prot'] = prot
        r = requests.post('http://127.0.0.1:4000/', data=data)
        return render_template('index.html')
    return data


@app.route('/get-file', methods=['GET', 'POST'])
def file():
    if request.method == 'POST':
        file = request.form['file']
        data['file'] = file
        r = requests.post('http://127.0.0.1:4000/', data=data)
        return render_template('index.html')
    return data


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
