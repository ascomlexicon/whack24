import pandas as pd
import preparation as prep


def main():
    df = prep.create_dataframe("assets\dataset.csv")


    print(getGoalsScoredBySeason(df))


if __name__ == "__main__":
    main()


def getMatch(oppostion, dataframe):
    return (dataframe.query('opposition_team == @opposition'))

def getMatch(matchId, dataframe):
    return (dataframe.query('match_id == @match_id'))

def getGoalsScoredBySeason(dataframe):
    return (dataframe.get("goals_scored, season_name"))

