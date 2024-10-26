from flask import Blueprint, render_template, request
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

home = Blueprint("home", __name__, template_folder="home_templates", static_folder="home_static")

@home.route("/")
def index():
    return render_template("index.html", data=["this", "is", "data"])

@home.route("/search")
def search():
    query = request.args.get("query")
    matches = []
    search_results = []
    filter = True

    if query: # If the user has entered a search query...
        matches = [] # ...load the matching matches to display.
        for match in matches:
            if fuzz.ratio(query, match.opponent_name) >= 90:
                location = request.args.get("location")
                season = request.args.get("season")
                result = request.args.get("result")

                if location != None:
                    if location != match.location:
                        filter = False
                if season != None:
                    if season != match.season_name:
                        filter = False
                if result != None:
                    if result != match.match_outcome:
                        filter = False

                if filter == True:                                
                    search_results.append(match)
                
    
    
    # <WIP: apply filters (home/away, season, win/loss)>

    return render_template("search.html", results=search_results, query=query)

