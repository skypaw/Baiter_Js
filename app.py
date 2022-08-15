from flask import Flask, make_response, render_template, request, redirect, url_for, render_template_string

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    r = make_response(render_template('index.html'))
    r.headers.set('X-Powered-By', 'Express')
    return r


@app.route("/login", methods=['GET', 'POST'])
def login_user():
    r = make_response(render_template('login.html'))
    r.headers.set('X-Powered-By', 'Express')
    if request.method == 'POST':
        return redirect(url_for('index'))
    return r


@app.after_request
def log(response):
    log_dictionary = {"User Agent": request.user_agent.__str__(),
                      "Ip": request.remote_addr,
                      "Path": request.full_path,
                      "Method": request.method,
                      "Request": request.json
                      }
    app.logger.warning(log_dictionary.__str__())
    return response


@app.route("/<path:path>", methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE'])
def catch_all(path):
    return render_template_string('Found')


@app.route("/register", methods=['GET', 'POST'])
def register_user():
    r = make_response(render_template('register.html'))
    r.headers.set('X-Powered-By', 'Express')
    if request.method == 'POST':
        return redirect(url_for('index'))
    return r


if __name__ == '__main__':
    app.run(port=5001)
