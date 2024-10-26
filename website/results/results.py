from flask import Blueprint, render_template, request
from ..datafunc.query import getMatch
from ..datafunc.preparation import clean_dataframe, create_dataframe
import pandas as pd


results = Blueprint("results", __name__, template_folder="results_templates", static_folder="results_static")
frame: pd.DataFrame = clean_dataframe(create_dataframe("assets/dataset.csv"))

def _get_match(id):
    for i in frame.index:
        if float(frame["match_id"][i]) == float(id):
            return i

@results.route("/match/<string:id>")
def match_page(id):
    # Get match from ID and pass in to template.
    tab = request.args.get("tab") or "summary"
    print(frame["Opposition"][_get_match(id)])
    return render_template("match.html", tab=tab, i=_get_match(id), frame=frame)