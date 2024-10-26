import pandas as pd
import matplotlib as plt
from ..datafunc.preparation import create_dataframe, clean_dataframe


def main():
    df = create_dataframe('assets/dataset.csv')
    clean_dataframe(df)

if __name__ == "__main__":
    main()