import base64
from flask import Blueprint, render_template
from io import BytesIO
from ..datafunc.graph import *
from ..datafunc.query import *

season = Blueprint("season", __name__, template_folder="season_templates", static_folder="season_static")

@season.route("/")
def season_home():
    dataframe = clean_dataframe(create_dataframe("assets/dataset.csv"))
    
    buf = graphGoalsBySeason(getGoalsScoredBySeason(dataframe))
    data = base64.b64encode(buf.getbuffer()).decode("ascii")

    buf = graphShotsPerSeason(getShotsPerSeason(dataframe))
    data1 = base64.b64encode(buf.getbuffer()).decode("ascii")

    buf = graphShotsTargPerSeason(getShotsTargPerSeason(dataframe))
    data3 = base64.b64encode(buf.getbuffer()).decode("ascii")


    buf = graphGoalsConcededPerSeason(getGoalsConcBySeason(dataframe))
    data4 = base64.b64encode(buf.getbuffer()).decode("ascii")


    buf = graphPassesPerSeason(getPassesBySeason(dataframe))
    data5 = base64.b64encode(buf.getbuffer()).decode("ascii")


    buf = graphBoxPassesPerSeason(getPassesInBoxBySeason(dataframe))
    data6 = base64.b64encode(buf.getbuffer()).decode("ascii")


    buf = graphTacklesPerSeason(getTacklesPerSeason(dataframe))
    data7 = base64.b64encode(buf.getbuffer()).decode("ascii")

    buf = graphGoalsBreakdown(dataframe)
    data9 = base64.b64encode(buf.getbuffer()).decode("ascii")

    buf = graphShotsOnTargBreakdown(dataframe)
    data10 = base64.b64encode(buf.getbuffer()).decode("ascii")

    return render_template("season_home.html", data=[data,data1,data3,data4,data5,data6,data7,data9,data10])

@season.route("/season/<int:seas>")
def season_page(seas):
    dataframe = clean_dataframe(create_dataframe("assets/dataset.csv")) 



    return render_template("season.html", seas=seas)