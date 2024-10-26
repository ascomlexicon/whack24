from flask import Blueprint, render_template, request
from fuzzywuzzy import fuzz
from ..datafunc.preparation import clean_dataframe, create_dataframe
import pandas as pd

home = Blueprint("home", __name__, template_folder="home_templates", static_folder="home_static")
frame: pd.DataFrame = clean_dataframe(create_dataframe("assets/dataset.csv"))

@home.route("/")
def index():
    return render_template("index.html", data=["this", "is", "data"])

@home.route("/search")
def search():
    query = request.args.get("query")
    search_results = []
    filter = True

    if query: # If the user has entered a search query...
        for i in frame.index:
            if fuzz.ratio(query, frame["opposition_team"][i]) >= 75 or fuzz.ratio(query.lower(), str(frame["Opposition"][i]).lower()) >= 75:
                location = request.args.get("location")
                season = request.args.get("season")
                result = request.args.get("result")

                if location != None:
                    if location != frame["location"][i]:
                        filter = False
                if season != None:
                    if season != frame["season_name"][i]:
                        filter = False
                if result != None:
                    if result != frame["match_outcomes"][i]:
                        filter = False

                if filter == True:                                
                    search_results.append(i)
    else:
        search_results = list(range(len(frame)))
    # <WIP: apply filters (home/away, season, win/loss)>

    return render_template("search.html", indices=search_results, frame=frame, query=query)

