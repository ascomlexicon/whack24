import pandas as pd


def getMatch(oppostion, dataframe):
    return (dataframe.query('opposition_team == @opposition'))

def getMatch(matchId, dataframe):
    for index in range(len(dataframe)):
        if dataframe.loc[index,'match_id'] == matchId:
            return dataframe.loc[index]
    return None
    # return (dataframe.query('match_id == @match_id'))

def getGoalsScoredBySeason(dataframe):
    return (dataframe.get(["goals_scored", "season_name"]))

