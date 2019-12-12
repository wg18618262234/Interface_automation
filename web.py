from flask import Flask, render_template

app = Flask(__name__)


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
    return render_template('index.html', code='1')


if __name__ == '__main__':
    app.run(port=5000)
