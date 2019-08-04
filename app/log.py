from flask import Flask, request, redirect, abort
app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])

    if user.check_password(request.form['password']):
        login_user(user)
        app.logger.info('%s logged in successfully', user.username)
        return redirect(url_for('index'))
    else:
        app.logger.info('%s failed to log in', user.username)
        abort(401)


def get_user(username):
    return username


def login_user(username):
    return username


def url_for(username):
    return username
