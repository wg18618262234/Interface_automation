import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    from unit.csvs import opencsvlist
    data = opencsvlist()
    head = data.pop(0)
    bodys = data
    return render_template('report.html', head=head, bodys=bodys)


@app.route('/start')
def start():
    from start import start
    start()
    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            basepath = os.path.dirname(__file__)
            file.save(os.path.join(basepath, app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    return '上传失败'


if __name__ == '__main__':
    app.run(port=5000)
