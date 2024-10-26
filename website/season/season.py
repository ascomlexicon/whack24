from flask import Blueprint, render_template

season = Blueprint("season", __name__, template_folder="season_templates", static_folder="season_static")

@season.route("/")
def season_home():
    return render_template("season_home.html")


@season.route("/season/<int:seas>")
def season_page(seas):
    return render_template("season.html", seas=seas)