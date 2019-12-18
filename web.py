import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

headers = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    from unit.csvs import open_csv_list, open_error_csv_list, open_success_csv_list
    data = open_csv_list()
    head = data.pop(0)
    data_success = open_success_csv_list()
    data_success.pop(0)
    data_error = open_error_csv_list()
    data_error.pop(0)
    return render_template('report.html', head=head, data_success=data_success, data_error=data_error)


@app.route('/start')
def start():
    from start import start
    start(headers)
    from unit.ding import send_message, get_sign
    from unit.csvs import get_count
    import time

    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    mes = "接口自动化测试报告\n" + \
          ">成功：" + str(get_count().get('success_count')) + "\n" + \
          ">失败：" + str(get_count().get('error_count')) + "\n\n" + \
          "测试报告地址：" + "http://0.0.0.0:5001/report\n" + \
          "![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png)\n" + \
          "###### " + t + " 发布 [测试报告](http://0.0.0.0:5001/report) \n"
    send_message(mes, timestamp=get_sign().get('timestamp'), sign=get_sign().get('sign'))
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


@app.route('/setheaders', methods=['GET', 'POST'])
def get_headers():
    global headers
    if request.method == 'POST':
        json_data = request.get_json()
        headers.update(json_data)
        json_data.update({'code': 1})
        return jsonify(json_data)
    return headers


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
