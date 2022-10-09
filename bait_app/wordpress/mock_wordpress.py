from flask import Blueprint, request, render_template_string, make_response, Response
import json

bp = Blueprint("mock_wordpress", __name__)

with open('bait_app/wordpress/mock_config.json', 'r') as config_file:
    CONFIG = json.load(config_file)


@bp.route("/WORDPRESS", methods=['GET', 'POST'])
@bp.route("/WP", methods=['GET', 'POST'])
@bp.route("/WordPress", methods=['GET', 'POST'])
@bp.route("/Wordpress", methods=['GET', 'POST'])
@bp.route("/Wp", methods=['GET', 'POST'])
@bp.route("/wp", methods=['GET', 'POST'])
@bp.route("/wordpress", methods=['GET', 'POST'])
@bp.route("/wp-1ogin_bak.php", methods=['GET', 'POST'])
@bp.route("/wp-booking.php", methods=['GET', 'POST'])
@bp.route("/wp-config.php", methods=['GET', 'POST'])
@bp.route("/wp-login.php", methods=['GET', 'POST'])
@bp.route("/wp-old.php", methods=['GET', 'POST'])
@bp.route("/wpindex.php?idb=https://raw.githubusercontent.com/carlosdechia/carlosdechia/main/ExV1",
          methods=['GET', 'POST'])
def wordpress_basic_path_response():
    return response_from_config(request.full_path, request.method)


@bp.route("/wp-config/<path:path>", methods=['GET', 'POST'])
@bp.route("/wp-content/<path:path>", methods=['GET', 'POST'])
@bp.route("/wp-includes/<path:path>", methods=['GET', 'POST'])
@bp.route("/wordpress/<path:path>", methods=['GET', 'POST'])
@bp.route("/wp-admin/<path:path>", methods=['GET', 'POST'])
@bp.route("/wp/<path:path>", methods=['GET', 'POST'])
def wordpress_simple_path_response(path):
    return response_from_config(request.full_path, request.method)


@bp.route("/<path:start>/wp-includes/<path:end>", methods=['GET', 'POST'])
def wordpress_path_response(start, end):
    return response_from_config(request.full_path, request.method)


def response_from_config(full_path, method):
    response = None
    if full_path in CONFIG:
        response_type = CONFIG[full_path]['response']
        if response_type == 'static-file':
            response = from_static()
    else:
        response = make_response(full_path)
    return response


def from_static():
    with open('bait_app/wordpress/static/wlwmanifest.xml', 'r') as file:
        a = file.read()
    return Response(a, mimetype='text/xml')
