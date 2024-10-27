from flask import Blueprint, render_template, request
from ..datafunc.query import getMatch
from ..datafunc.preparation import clean_dataframe, create_dataframe
import pandas as pd
import json


results = Blueprint("results", __name__, template_folder="results_templates", static_folder="results_static")
frame: pd.DataFrame = clean_dataframe(create_dataframe("assets/dataset.csv"))


@results.route("/match/<string:id>")
def match_page(id):
    # Get match from ID and pass in to template.
    tab = request.args.get("tab") or "summary"
    match = getMatch(float(id), frame)

    
    return render_template("match.html", tab=tab, match=match, lineup=format_lineup(match.get("lineup")))


def format_lineup(lineup: str):
    lineup_arr = [[], [], [], [], [], []] # goal, back, mid, front, subs, unused
    for player in json.loads(lineup.replace("'", "\"")):
        if player["position"].lower() == "goalkeeper" and "Starting" in player["squad_role"]:
            lineup_arr[0].append(player)
        elif "back" in player["position"].lower() and "Starting" in player["squad_role"]:
            lineup_arr[1].append(player)
        elif "midfield" in player["position"].lower() and "Starting" in player["squad_role"]:
            lineup_arr[2].append(player)
        elif ("wing" in player["position"].lower() or "forward" in player["position"].lower()) and "Starting" in player["squad_role"]:
            lineup_arr[3].append(player)
        else:
            if "unused" in player["squad_role"].lower(): # unused
                lineup_arr[5].append(player)
            else: # sub
                lineup_arr[4].append(player)
    # for i in lineup_arr:
    #     for x in i:
    #         print(x)
    #     print("\n")
        
    return lineup_arr