import pandas as pd
import numpy as np

#----Inspect
def summarize(df):
    df = df.copy()
    missing_data = (df.isna().mean() *100).round(2).to_dict()
    print(f'\n----Column Titles: \n{list(df.columns)}\n\n')
    print('----Missing Percentages:\n')
    for key, value in missing_data.items():
        print(f'{key}, {value}% missing')
    print('\n----Data Types:\n\n', df.dtypes, '\n\n')
    print(df.describe(include='all'), '\n\n')
    print(df.info())