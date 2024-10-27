import numpy as np
import scipy as sp
import pandas as pd
from ..datafunc.query import getMatch

def finishing_effectiveness(dataframe, matchID):
    game = getMatch(matchID, dataframe)
    
    difference = float(game["goals_scored"] - game["np_xg"])
    
    goal_list = dataframe["goals_scored"].tolist()
    xg_list = dataframe["np_xg"].tolist()
    
    performances = list(map(lambda t: t[0] - t[1], zip(goal_list, xg_list)))
    
    percentile = round(float(sp.stats.percentileofscore(performances, difference)), 2)
    
    if percentile >= 60:
        return percentile, "The team overperformed their xG."
    elif percentile >= 40:
        return percentile, "Average finishing."
    else:
        return percentile, "Poor finishing, work on converting chances."

def creating_chances(dataframe, matchID):
    game = getMatch(matchID, dataframe)

    percentile = round(float(sp.stats.percentileofscore(dataframe["np_xg"], game["np_xg"])), 2)
    
    if percentile >= 60:
        return percentile, "The team created many chances."
    elif percentile >= 40:
        return percentile, "Created the usual number of chances."
    else:
        return percentile, "You are struggling to break through the defence of the opposition."

def set_piece_defense(dataframe, matchID):
    game = getMatch(matchID, dataframe)
    
    set_piece_xG = float(game["xg_conceded_within_8_seconds_of_corner"] + game["xg_conceded_within_8_seconds_of_indirect_free_kick"])
    
    corner_list = dataframe["xg_conceded_within_8_seconds_of_corner"].tolist()
    freekick_list = dataframe["xg_conceded_within_8_seconds_of_indirect_free_kick"].tolist()

    performances = list(map(lambda t: t[0] + t[1], zip(corner_list, freekick_list)))
    
    percentile = round(float(sp.stats.percentileofscore(performances, set_piece_xG)), 2)
    
    if percentile <= 60:
        return percentile, "The team is struggling to defend set-pieces"
    elif percentile <= 40:
        return percentile, "Average defending."
    else:
        return percentile, "Strong defense against set-pieces."

def pressing_effectiveness(dataframe, matchID):
    game = getMatch(matchID, dataframe)
    
    percentile = round(float(sp.stats.percentileofscore(dataframe["ppda"], game["ppda"])), 2)
    
    if percentile <= 60:
        return percentile, "The team is either not pressing or are not pressing effectively"
    elif percentile <= 40:
        return percentile, "Presses are average."
    else:
        return percentile, "You are effectively winning the ball back."

def shot_accuracy(dataframe, matchID):
    game = getMatch(matchID, dataframe)
    
    shot_acc = float(game["shots_on_target"] / game["shots"])
    
    accurate_list = dataframe["shots_on_target"].tolist()
    shot_list = dataframe["shots"].tolist()

    performances = list(map(lambda t: t[0] / t[1], zip(accurate_list, shot_list)))
    
    percentile = round(float(sp.stats.percentileofscore(performances, shot_acc)), 2)

    if percentile >= 60:
        return percentile, "The team were very accurate with their shooting."
    elif percentile >= 40:
        return percentile, "Average accuracy."
    else:
        return percentile, "Poor shooting accuracy."


def possession(dataframe, matchID):
    game = getMatch(matchID, dataframe)

    percentile = round(float(sp.stats.percentileofscore(dataframe["possession"], game["possession"])), 2)
     
    if percentile >= 60:
        return percentile, "The team has good possession"
    elif percentile >= 40:
        return percentile, "Standard possession."
    else:
        return percentile, "Possesssion is subpar."
