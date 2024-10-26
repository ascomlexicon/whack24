from flask import Blueprint, render_template

home = Blueprint("home", __name__, template_folder="home_templates", static_folder="home_static")

@home.route("/")
def index():
    return render_template("index.html", data=["this", "is", "data"])