import numpy as np
import pandas as pd
from dataconstants import IGNORE_COLUMNS

def create_dataframe(filepath):
    dataframe = pd.read_csv(filepath, index_col=0)
    
    dataframe = dataframe.drop(columns=IGNORE_COLUMNS)
    
    return dataframe

def clean_dataframe(dataframe):
    clean_frame = dataframe.dropna()
    
    clean_frame["match_outcome"] = np.where(
        clean_frame["match_outcome"].str.contains("lost"), clean_frame["match_outcome"].str.replace("lost", "L"), np.where(
            clean_frame["match_outcome"].str.contains("won"), clean_frame["match_outcome"].str.replace("won", "W"), clean_frame["match_outcome"].str.replace("draw", "D")   
        ) 
    )
    
    clean_frame["location"] = np.where(
        clean_frame["location"].str.contains("away"), clean_frame["location"].str.replace("away", "A"), clean_frame["location"].str.replace("home", "H")
    )

    return clean_frame.reset_index(drop=True)
