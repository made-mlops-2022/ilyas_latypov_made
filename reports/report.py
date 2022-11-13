import pandas as pd
from pandas_profiling import ProfileReport

def report():

    profile = ProfileReport(pd.read_csv(r'..\data_for_modeling\data\heart_cleveland_upload.csv'))
    profile.to_file("report.html")


if __name__ == "__main__":
    report()