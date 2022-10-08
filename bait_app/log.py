from flask import Blueprint, request, current_app

bp = Blueprint("log", __name__)


@bp.after_request
def log(response):
    log_dictionary = {"User Agent": request.user_agent.__str__(),
                      "Ip": request.remote_addr,
                      "Path": request.full_path,
                      "Method": request.method,
                      }
    current_app.logger.warning(log_dictionary.__str__())
    return response
