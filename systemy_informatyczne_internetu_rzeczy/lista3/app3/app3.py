from flask import Flask, request, json
app = Flask(__name__)

stat = {}


@app.route('/',  methods=['GET', 'POST'])
def my_test_endpoint():
    if request.method == 'POST':
        input = json.loads(request.data.decode('utf-8'))
        stat['pc'] = input
        return input
    return stat


if __name__ == '__main__':
    app.run(debug=True)
