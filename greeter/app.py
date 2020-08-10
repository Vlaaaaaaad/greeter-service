import os
import json
from flask import Flask

HTTP_OK = 200


def make_app():
    app = Flask(__name__)
    app.VERSION = os.getenv('VERSION', 'dev')

    @app.route('/status/alive', methods=['GET'])
    def alive():
        data = {
            'status': 'Greeter service is alive',
        }

        return app.response_class(
            response=json.dumps(data),
            status=HTTP_OK,
            mimetype='application/json',
        )

    @app.route('/status/healthy', methods=['GET'])
    def healthy():
        data = {
            'status': 'Greeter service is healthy',
        }

        return app.response_class(
            response=json.dumps(data),
            status=HTTP_OK,
            mimetype='application/json',
        )

    @app.route('/', methods=['GET'])
    def index():
        data = {
            'greeting': 'hello',
        }

        return app.response_class(
            response=json.dumps(data),
            status=HTTP_OK,
            mimetype='application/json',
        )

    @app.after_request
    def after_request_func(response):
        response.headers['X-Reply-Service'] = 'greeter-service'
        response.headers['X-Version'] = app.VERSION
        return response

    return app
