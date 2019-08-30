from flask import Flask,render_template

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_world(name=None):
    return name


if __name__ == '__main__':
    app.run()
