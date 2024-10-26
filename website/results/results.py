from flask import Blueprint, render_template, request

results = Blueprint("results", __name__, template_folder="results_templates", static_folder="results_static")

@results.route("/match")
def match_page():
    tab = request.args.get("tab") or "summary"
    print(tab)
    return render_template("match.html", tab=tab)