import numpy as np
import pandas as pd

def average_stats_against_opposition(dataframe, team, column, keep_home=False):
    if column not in list(dataframe.columns):
        raise ValueError("Column not in dataframe!")
    
    
    if team.lower() not in map(lambda s: s.lower(), dataframe["opposition_team"].tolist()):
        raise ValueError("Not a valid team!")

    team_df = dataframe.copy()
    
    if not keep_home:
        team_df = team_df.query(f"location != 'H'")
    
    team_df = team_df.query(f"opposition_team == '{team}'")

    return round(np.mean(team_df[column].tolist()), 3)

def total_stats_against_opposition(dataframe, team, column):
    if column not in list(dataframe.columns):
        raise ValueError("Column not in dataframe!")
    
    if team.lower() not in map(lambda s: s.lower(), dataframe["opposition_team"].tolist()):
        raise ValueError("Not a valid team!")
    
    team_df = dataframe.query(f"opposition_team == {team}")

    return round(sum(team_df[column].tolist()), 3)
