from flask import Flask, make_response, render_template, request, redirect, url_for, render_template_string

from bait_app import auth

app = Flask(__name__)
app.register_blueprint(auth.bp)


@app.route("/", methods=['GET'])
def index():
    r = make_response(render_template('index.html'))
    r.headers.set('X-Powered-By', 'Express')
    return r


@app.after_request
def log(response):
    log_dictionary = {"User Agent": request.user_agent.__str__(),
                      "Ip": request.remote_addr,
                      "Path": request.full_path,
                      "Method": request.method,
                      }
    app.logger.warning(log_dictionary.__str__())
    return response


@app.route("/<path:path>", methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE'])
def catch_all(path):
    return render_template_string('Found')


if __name__ == '__main__':
    app.run(port=5001)
