from flask import make_response, render_template
from functools import wraps


def set_headers(template):
    def decorator(function):
        @wraps(function)
        def header_wrapper():
            response = make_response(render_template(template))
            response.headers.set('X-Powered-By', 'Express')
            return function(response)

        return header_wrapper

    return decorator
