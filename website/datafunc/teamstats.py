import numpy as np
import pandas as pd

def average_stats_against_opposition(dataframe, team, column):
    if column not in list(dataframe.tolist()):
        raise ValueError("Column not in dataframe!")
    
    if team.lower() not in map(lambda s: s.lower(), dataframe["Opposition"].tolist()):
        raise ValueError("Not a valid team!")
    
    team_df = dataframe.query(f"Opposition == {team}")

    return round(np.mean(team_df[column].tolist()), 3)

def total_stats_against_opposition(dataframe, team, column):
     if column not in list(dataframe.tolist()):
        raise ValueError("Column not in dataframe!")
    
    if team.lower() not in map(lambda s: s.lower(), dataframe["Opposition"].tolist()):
        raise ValueError("Not a valid team!")
    
    team_df = dataframe.query(f"Opposition == {team}")

    return round(sum(team_df[column].tolist()), 3)
