from flask import Blueprint, request, render_template_string

bp = Blueprint("mock_wordpress", __name__)


@bp.route("/wp-config<path:path>", methods=['GET', 'POST'])
@bp.route("/wordpress<path:path>", methods=['GET', 'POST'])
def mock_wordpress(path):
    response = response_from_config(request.full_path, request.method)

    return response


def response_from_config(full_path, method):
    return render_template_string('')
