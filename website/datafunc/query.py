import pandas as pd


def getMatch(oppostion, dataframe):
    return (dataframe.query('opposition_team == @opposition'))

def getMatch(match_id, dataframe):
    return (dataframe.query('match_id == @match_id'))

def getGoalsScoredBySeason(dataframe):
    return (dataframe.get(["goals_scored", "season_name"]))

