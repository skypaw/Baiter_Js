from flask import Blueprint, request, make_response, render_template, redirect, url_for
from .decorators import set_headers

bp = Blueprint("auth", __name__, url_prefix='')


@bp.route("/register", methods=['GET', 'POST'])
@set_headers('register.html')
def register_user(r):
    if request.method == 'POST':
        return redirect(url_for('index'))
    return r


@bp.route("/login", methods=['GET', 'POST'])
@set_headers('login.html')
def login_user(r):
    if request.method == 'POST':
        return redirect(url_for('index'))
    return r
