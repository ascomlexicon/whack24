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

def getShotsPerSeason(dataframe):
    return (dataframe.get(["shots", "season_name"]))

def getShotsTargPerSeason(dataframe):
    return (dataframe.get(["shots_on_target", "season_name"]))

def getGoalsConcBySeason(dataframe):
    return (dataframe.get(["goals_conceded", "season_name"]))

def getPassesBySeason(dataframe):
    return (dataframe.get(["passes", "season_name"]))

def getPassesInBoxBySeason(dataframe):
    return (dataframe.get(["completed_passes_into_the_box", "season_name"]))

def getTacklesPerSeason(dataframe):
    return (dataframe.get(["tackles", "season_name"]))

def getWinStats(dataframe):
    return (dataframe.get(["match_outcome", "season_name"]))

def getGoalStatsFromMatch(dataframe, id):

    match = getMatch(id, dataframe)

    return match['goals_scored'], match['goals_conceded']


def getShotStatsFromMatch(dataframe, id):

    match = getMatch(id, dataframe)

    return match['shots'], match['shots_on_target']


def getOppShotStatsFromMatch(dataframe, id):

    match = getMatch(id, dataframe)

    return match['opposition_shots'], match['opposition_shots_on_target']


def getPossesionFromMatch(dataframe, id):

    match = getMatch(id, dataframe)

    return match['possession'], (100- match['possession'])


def getPossesionThirdFromMatch(dataframe, id):

    match = getMatch(id, dataframe)

    return match['final_third_possession'], (100- match['final_third_possession'])



