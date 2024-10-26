from flask import Blueprint, render_template, request

home = Blueprint("home", __name__, template_folder="home_templates", static_folder="home_static")

@home.route("/")
def index():
    return render_template("index.html", data=["this", "is", "data"])

@home.route("/search")
def search():
    query = request.args.get("search")
    search_results = []
    if query: # If the user has entered a search query...
        search_results = [] # ...load the matching matches to display.
    
    # <WIP: apply filters>

    return render_template("search.html", results=search_results)