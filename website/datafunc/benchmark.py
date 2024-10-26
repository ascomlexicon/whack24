import numpy as np
import pandas as pd
from sklearn import linear_model
import preparation as p

def benchmark_range_for_season(dataframe, column, season):
    if column not in list(dataframe.columns):
        raise ValueError("Column not found in table")
    
    seasons = set(dataframe["season_name"].tolist())

    if season not in seasons:
        raise ValueError("Not a valid season!")
    
    filtered_df = dataframe.query(f"season_name == {season}")

    required_data = filtered_df[column].tolist()

    maximum = np.max(required_data)
    mean = np.mean(required_data)
    minimum = np.min(required_data)
    
    return round(float(maximum), 2), round(float(mean), 2), round(float(minimum), 2) 

def benchmark_range_column(dataframe, column):
    if column not in list(dataframe.columns):
        raise ValueError("Column not found in table")
    
    required_data = dataframe[column].tolist()

    maximum = np.max(required_data)
    mean = np.mean(required_data)
    minimum = np.min(required_data)
    
    return round(float(maximum), 2), round(float(mean), 2), round(float(minimum), 2) 

def season_win_percentage(dataframe, season):
    if season not in set(dataframe["season_name"].tolist()):
        raise ValueError("Not a valid season!")
    
    filtered_df = dataframe.query(f"season_name == {season}")

    return round(len(filtered_df.query("match_outcome == 'W'")) / len(filtered_df), 2)

def season_unbeaten_percentage(dataframe, season):
    if season not in set(dataframe["season_name"].tolist()):
        raise ValueError("Not a valid season!")
    
    filtered_df = dataframe.query(f"season_name == {season}")

    return round(len(filtered_df.query("match_outcome != 'L'")) / len(filtered_df), 2)

def column_correlation(dataframe, columnX, columnY):
    if columnX not in list(dataframe.columns):
        raise ValueError(f"{columnX} not found in table")
    
    if columnY not in list(dataframe.columns):
        raise ValueError(f"{columnY} not found in table")


    x = dataframe[columnX].values.reshape(len(df), 1)
    y = dataframe[columnY].values.reshape(len(df), 1)
    
    regression = linear_model.LinearRegression()
    regression = regression.fit(x, y)
    
    correlation = regression.score(x, y)
    coefficients = regression.coef_
    
    return correlation, coefficients
    
if __name__ == "__main__":
    df = p.clean_dataframe(p.create_dataframe("assets/dataset.csv"))
    
    print(column_correlation(df, "final_third_possession", "np_xg"))
