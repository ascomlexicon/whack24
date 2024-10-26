import numpy as np
import pandas as pd
import preparation as p

def benchmark_range(dataframe, column, season):
    if column not in list(dataframe.columns):
        raise ValueError("Column not found in table")
    
    seasons = set(dataframe["season_name"].tolist())

    if season not in seasons:
        raise ValueError("Not a valid season!")
    
    filtered_df = dataframe.query(f"season_name == {season}")

    required_data = filtered_df[column].tolist()

    low_five_percentile = np.percentile(required_data, 5)
    mean = np.mean(required_data)
    high_five_percentile = np.percentile(required_data, 95)
    
    return round(float(low_five_percentile), 3), round(float(mean), 2), round(float(high_five_percentile), 3) 
