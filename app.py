from flask import Flask, make_response, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    app.logger.warning(request.user_agent)
    r = make_response(render_template('index.html'))
    r.headers.set('X-Powered-By', 'Express')
    return r


@app.route("/login", methods=['GET', 'POST'])
def login_user():
    app.logger.warning(request.user_agent)
    r = make_response(render_template('login.html'))
    r.headers.set('X-Powered-By', 'Express')
    if request.method == 'POST':
        app.logger.warning(request.form)
        return redirect(url_for('index'))
    return r


@app.errorhandler(500)
@app.errorhandler(404)
def not_found(e):
    app.logger.warning(request.user_agent)
    app.logger.warning(request.headers)


@app.route("/register", methods=['GET', 'POST'])
def register_user():
    app.logger.info(request.user_agent)
    r = make_response(render_template('register.html'))
    r.headers.set('X-Powered-By', 'Express')
    if request.method == 'POST':
        app.logger.warn(request.form)
        return redirect(url_for('index'))
    return r


if __name__ == '__main__':
    app.run(port=5001)
