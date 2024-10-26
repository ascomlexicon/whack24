from flask import Flask
from os import environ


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = environ.get("SECRET_KEY")

    from .results.results import results
    from .home.home import home
    from .season.season import season

    app.register_blueprint(results, url_prefix="/results")
    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(season, url_prefix="/season")

    return app