from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('download.html')


@app.route('/download')
def download():
    p = 'TO_UPLOAD.txt'
    return send_file(p, as_attachment=True)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
