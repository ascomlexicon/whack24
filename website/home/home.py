from flask import Blueprint

home = Blueprint("home", __name__, template_folder="home_templates", static_folder="home_static")

