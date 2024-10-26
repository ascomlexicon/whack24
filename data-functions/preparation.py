import pandas as pd
from dataconstants import IGNORE_COLUMNS

def create_dataframe(filepath):
    dataframe = pd.read_csv(filepath, index_col=0)
    
    dataframe = dataframe.drop(columns=IGNORE_COLUMNS)
    
    return dataframe

def clean_dataframe(dataframe):
    clean_frame = dataframe.dropna()
    return clean_frame.reset_index(drop=True)
