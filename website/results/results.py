from flask import Blueprint

results = Blueprint("results", __name__, template_folder="home_templates", static_folder="home_static")

