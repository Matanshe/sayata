from flask import Flask

from routes import submission_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(submission_bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
