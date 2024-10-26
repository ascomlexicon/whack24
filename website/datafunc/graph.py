import pandas as pd
import matplotlib as plt
import preparation as prep
import query as query


def main():
    df = prep.create_dataframe('assets/dataset.csv')
    prep.clean_dataframe(df)

if __name__ == "__main__":
    main()