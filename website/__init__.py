from flask import Flask
from os import environ


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = environ.get("SECRET_KEY")

    from .results.results import results
    from .home.home import home

    app.register_blueprint(results, url_prefix="/results")
    app.register_blueprint(home, url_prefix="/")


    return app