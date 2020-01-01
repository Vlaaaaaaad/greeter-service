from flask import Flask


def make_app():
    app = Flask(__name__)

    @app.route('/status/alive')
    def alive():
        return 'Application is alive'

    @app.route('/status/healthy')
    def healthy():
        return 'Application is healthy'

    @app.route('/')
    def index():
        return 'Hello'

    return app


if __name__ == '__main__':
    app = make_app()
    app.run(port=5002)
