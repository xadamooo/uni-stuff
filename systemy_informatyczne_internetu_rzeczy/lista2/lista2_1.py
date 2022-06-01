import os
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
path = os.getcwd()
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['UPLOAD_FOLDER'] = path
ALLOWED_EXTENSIONS = set(['txt'])


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('/')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
