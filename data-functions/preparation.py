import pandas as pd
from dataconstants import IGNORE_COLUMNS

def create_dataframe() -> pd.DataFrame:
    dataframe = pd.read_csv("assets/dataset.csv")
    
    dataframe = dataframe.drop(columns=IGNORE_COLUMNS)
    
    return dataframe

if __name__ == "__main__":
    create_dataframe()