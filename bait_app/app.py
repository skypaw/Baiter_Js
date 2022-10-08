from flask import Flask, make_response, render_template, render_template_string, request

from bait_app import auth

app = Flask(__name__)
app.register_blueprint(auth.bp)


@app.route("/", methods=['GET'])
def index():
    r = make_response(render_template('index.html'))
    r.headers.set('X-Powered-By', 'Express')
    return r


@app.route("/<path:path>", methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE'])
def catch_all(path):
    return render_template_string('Found')


@app.after_request
def log(response):
    request_data = {"User Agent": request.user_agent.__str__(),
                    "Ip": request.remote_addr,
                    "Path": request.full_path,
                    "Method": request.method,
                    "Form": request.form,
                    "Cookies": request.cookies,
                    "RequestHeaders": request.headers.__str__(),
                    }
    app.logger.warning(request_data)
    return response


if __name__ == '__main__':
    app.run(port=5001)
