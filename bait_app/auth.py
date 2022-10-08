from flask import Blueprint, request, make_response, render_template, redirect, url_for

bp = Blueprint("auth", __name__, url_prefix='')


@bp.route("/register", methods=['GET', 'POST'])
def register_user():
    r = make_response(render_template('register.html'))
    r.headers.set('X-Powered-By', 'Express')
    if request.method == 'POST':
        return redirect(url_for('index'))
    return r


@bp.route("/login", methods=['GET', 'POST'])
def login_user():
    r = make_response(render_template('login.html'))
    r.headers.set('X-Powered-By', 'Express')
    if request.method == 'POST':
        return redirect(url_for('index'))
    return r
