from flask import Blueprint, render_template, request

season = Blueprint("season", __name__, template_folder="season_templates", static_folder="season_static")

@season.route("/")
def season_page():
    search_results=[]

    return render_template("season.html", results=search_results)
